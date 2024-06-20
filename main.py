import sys
import os
import smtplib
import ssl

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QDialog, QHeaderView,QHBoxLayout,  QSpacerItem, QSizePolicy
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView

from getmac import get_mac_address as gma

import datetime
from datetime import datetime, timedelta
import time
from sqlalchemy import text
import pandas as pd

import concurrent.futures
from tkinter import Tk, filedialog

from charts import graphs
from plc_data_ui import Ui_MainWindow
from database import db_con as db_con
from authorization import auth
from interrupts import timer as timer
from plc_connection import snap7_plc as snap7_plc
from utils import Report as Report
from utils import mail as mail

import snap7

import struct



executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)

class PLCDataLogger(QtWidgets.QMainWindow, QDialog):
    def __init__(self): 
        super(PLCDataLogger, self).__init__()
        uic.loadUi('Welcome_plc.ui', self)

        idfont = QFontDatabase.addApplicationFont(
             "open-sans/Opensans-Semibold.ttf")
                
        
        if idfont < 0:
            print("Font Error")
        families = QFontDatabase.applicationFontFamilies(idfont)
        print("Font Family name : ", families[0])
        self.setFont(QFont("Open Sans"))



        self.logcon = self.findChild(QtWidgets.QTextEdit, 'connStatus')

        

        self.activateLicense.clicked.connect(self.insertKey)
        self.btnConnectDb.clicked.connect(self.openConnect)
        self.btnConnectDb.clicked.connect(timer.timerTable)  

    def openConnect(self):
        try:
            self.cursorRead, self.cursorWrite, self.engineConRead, self.engineConWriten, self.conn = db_con.dbConnection()
            
            query = text('SELECT * FROM Info_DB')
            self.dfInfo = pd.read_sql_query(query, self.engineConRead)
            print(self.dfInfo)
            self.day_bal, self.auth_status, self.softwaretype  = auth.authentication_main(self.dfInfo)
            print(self.day_bal, self.auth_status, self.softwaretype)
            cursorWrite = self.cursorWrite
            db_con.archive_old_data(cursorWrite)
            if self.auth_status == 1:
                self.openWindow()
            else:
                print(self.day_bal, self.auth_status)
        except Exception as e:
            print(f"Error updating license: {e}")


    def insertKey(self):
        try:
            self.cursorRead, self.cursorWrite, self.engineConRead, self.engineConWriten = db_con.dbConnection()
            lic = self.licenseEnter.text()
            query = "UPDATE Info_DB SET Info = ? WHERE CAST(Particulars AS NVARCHAR(MAX)) = ?"
            # Execute the query with parameters
            self.cursor.execute(query, (lic, "Activation_Key"))
            self.cursor.commit()
            db_con.archive_old_data(self.cursorWrite)
            print("DB Updated")
        except:
            print("DB Error")


    def openWindow(self):
        try:
            
            self.window = QtWidgets.QMainWindow()
            self.Ui = Ui_MainWindow()
            self.Ui.setupUi(self.window)
            Mainwindow.hide()
            idfont = QFontDatabase.addApplicationFont(
            "open-sans/Opensans-Semibold.ttf")
        
            if idfont < 0:
                print("Font Error")
            families = QFontDatabase.applicationFontFamilies(idfont)
            print("Font Family name : ", families[0])
            self.setFont(QFont("Open Sans"))
            self.window.show()
            revision =  self.dfInfo.loc[1, 'Info']
            print(revision)
            self.versionSet = self.Ui.versionSet
            self.versionSet.setText(revision)
            Licence = self.dfInfo.loc[4, 'Info']
            self.Ui.licenseEnter.setText(Licence)
            
            self.Ui.progressBar.hide()
            
            self.logImp = self.Ui.logImp
            self.logField = self.Ui.logField
            self.log = self.Ui.textStatus
         
#             self.Ui.btnDownloadExcel.clicked.connect(self.modelExcel)
#             self.Ui.activateLicense.clicked.connect(self.licence_main)                                       
 
            self.Ui.navHome.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.homePage))
            self.Ui.navExport.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.exportPage))
            self.Ui.navLog.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.logPage))
            self.Ui.navHelp.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.helpPage))
            self.Ui.navImp.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.importPage))
            self.Ui.navAbout.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.aboutPage))
            
            
            self.Ui.show_data_btn.clicked.connect(lambda: self.thread_and_handle(self.show_data))
            self.Ui.export_btn.clicked.connect(lambda: self.thread_and_handle(self.export_data))
            self.Ui.btnConnect.clicked.connect(lambda: self.thread_and_handle(self.plcConnect))
            # self.Ui.btnConnect.clicked.connect(timer.timer_logging)
            self.Ui.btnConnect.clicked.connect(self.timer_logging)
            self.Ui.btnDisconnect.clicked.connect(lambda: self.thread_and_handle(self.plcDisconnect))            
            self.Ui.btnClearLog.clicked.connect(self.clear_logs)
            self.Ui.btnDownloadReport.clicked.connect(lambda: self.thread_and_handle(self.report_dwn))
            self.Ui.btnShowGraph.clicked.connect(self.graph)
            self.Ui.btnBackup.clicked.connect(self.select_backup_path)
            self.Ui.navHome.clicked.connect(self.speedGraph)
            self.Ui.navHome.clicked.connect(self.barGraph)
            self.Ui.btnImpExcel.clicked.connect(self.open_excel_file)

            
            
#         else:
#             self.logcon.append('Error Licence expired: Contact admin')

        except Exception as e:
            print(f"Error on opening: {e}")




#################################      Therading The Functions       ##################################################
    def thread_and_handle(self, func):
        future = executor.submit(func)
        future.add_done_callback(self.handle_result)

    def handle_result(self, future):
        connStatus = future.result()  # Get the result from the future
        print(connStatus)

######################################      Table View       ################################################################
    def show_data(self):
        try:
            self.Ui.progressBar.show()
            hours = self.Ui.hrSelect.currentText()
            from_time = self.Ui.from_time.dateTime().toString(Qt.ISODate)
            to_time = self.Ui.to_time.dateTime().toString(Qt.ISODate)
            print(hours, from_time, to_time,self.engineConRead)
            self.df = db_con.show_data(hours, from_time, to_time, self.engineConRead)
            
            # Set up the DataFrame and model for display
            df = self.df
            self.model = PandasTableModel(df)
            self.Ui.table_view.setModel(self.model)            

            # Set column widths for better display
            self.Ui.table_view.setColumnWidth(0, 150)
            self.Ui.table_view.setColumnWidth(1, 300)
            self.Ui.table_view.setColumnWidth(2, 500)
            self.Ui.table_view.setColumnWidth(3, 150)
            self.Ui.table_view.setColumnWidth(4, 150)

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.Ui.progressBar.hide()

    def export_data(self):
        from_time = self.Ui.from_time.dateTime().toString(Qt.ISODate)
        to_time = self.Ui.to_time.dateTime().toString(Qt.ISODate)
        try:
            self.df = db_con.export_data(self.engineConRead, from_time, to_time)
            if self.df is None:
                return  # No data to export
                
            # Export DataFrame to Excel file
            file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel files (*.xlsx)")
            if file_name:
                self.df.to_excel(file_name, index=False)
            self.Ui.progressBar.hide()
        except Exception as e:
                self.logImp.append(f"Error: {e}")
    
    def report_dwn(self):
        try:
            self.Ui.progressBar.show()
            hours = self.Ui.hrSelect.currentText()
            from_time = self.Ui.from_time.dateTime().toString(Qt.ISODate)
            to_time = self.Ui.to_time.dateTime().toString(Qt.ISODate)
            self.df = db_con.show_data(hours, from_time, to_time, self.engineConRead)

            Report.Reportgen(from_time, to_time, self.df)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.Ui.progressBar.hide()

#####################################    PLC CONNECTION    #####################################################################
   
    def plcConnect(self):
        try:
            self.dfPlcdb = db_con.dfPlc(self.engineConRead, self.softwaretype)
            self.plcIP = self.Ui.inpIp.text()
            self.rackandslot = self.Ui.inpRackSlot.text()
            if self.plcIP == "" or self.rackandslot == "":
                self.rackandslot = self.dfInfo.loc[5, 'Info']

                rack, slot = map(int, self.rackandslot.split(','))
                # rack, slot = int(rack, slot)
                print(rack, slot)
                self.plcIP = self.dfInfo.loc[0, 'Info']
                print(self.plcIP)
                current_date = datetime.now()
               
                self.plc = snap7_plc.snap7Connect(self.plcIP, rack, slot)
                
                message = 'Info  - '  + str(current_date) + ' -  PLC is connected ' 
                self.log.append(message)
                self.log_to_file(message)
                self.local_connStatus = True
                self.run_logging()

            elif self.plcIP and self.rackandslot:
                query = "UPDATE Info_DB SET Info = ? WHERE CAST(Particulars AS NVARCHAR(MAX)) = ?"
                self.cursorWrite.execute(query, (self.rackandslot, "Rack _slot"))
                self.cursorWrite.commit()

                
                query = "UPDATE Info_DB SET Info = ? WHERE CAST(Particulars AS NVARCHAR(MAX)) = ?"
                # Execute the query with parameters
                self.cursorWrite.execute(query, (self.plcIP, "Plc_IP"))
                self.cursorWrite.commit()

                rack, slot = map(int, self.rackandslot.split(','))

                current_date = datetime.now()
                self.plc = snap7_plc.snap7Connect(self.plcIP, rack, slot)

                message = 'Info  - '  + str(current_date) + ' -  PLC is connected ' 
                self.log.append(message)
                self.log_to_file(message)
                self.local_connStatus = True
                self.run_logging()

            elif self.plcIP :                                
                query = "UPDATE Info_DB SET Info = ? WHERE CAST(Particulars AS NVARCHAR(MAX)) = ?"
                # Execute the query with parameters
                self.cursorWrite.execute(query, (self.plcIP, "Plc_IP"))
                self.cursorWrite.commit()

                rack, slot = map(int, self.rackandslot.split(','))

                current_date = datetime.now()
                self.plc = snap7_plc.snap7Connect(self.plcIP, rack, slot)

                message = 'Info  - '  + str(current_date) + ' -  PLC is connected ' 
                self.log.append(message)
                self.log_to_file(message)
                self.local_connStatus = True
                self.run_logging()

            elif self.rackandslot:
                query = "UPDATE Info_DB SET Info = ? WHERE CAST(Particulars AS NVARCHAR(MAX)) = ?"
                self.cursorWrite.execute(query, (self.rackandslot, "Rack _slot"))
                self.cursorWrite.commit()               
                
                rack, slot = map(int, self.rackandslot.split(','))

                current_date = datetime.now()
                self.plc = snap7_plc.snap7Connect(self.plcIP, rack, slot)

                message = 'Info  - '  + str(current_date) + ' -  PLC is connected ' 
                self.log.append(message)
                self.log_to_file(message)
                self.local_connStatus = True
                self.run_logging()


            else:
                self.log.append(f'PLC IP: {e}') 
                print("PLC IP address is not provided.")

            self.run_logging()
            
        except Exception as e:
            self.log.append(f'PLC is not connected: {e}') 
            print("Not connecting", e)
            self.local_conn == False
            self.logField.append(f"Error : {e}")
            print(self.dfPlcdb)

    def plcDisconnect(self):
        try:
            self.current_date = datetime.now()
            self.plc.disconnect()            
            self.local_connStatus = False
            self.monitor_timer.stop()
            # message = 'PLC data fetching Disconnected' + str(self.current_date)
            message = '"Alert"  - '  + str(self.current_date) + ' -  PLC is Disconnected ' 
            self.log.append(message)
            self.log_to_file(message)
        except Exception as e:
            self.log.append('PLC is Disconnected Error: {e}')
            print("Error while disconnecting:", e)
            self.local_connStatus = False
            
        return self.local_connStatus
          
    def run_logging(self):
        try:
            if self.local_connStatus == True:
                self.current_date = datetime.now()
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                # message = 'Logging  - '  + str(timestamp) + ' -  Data fetching from PLC ' 
                # self.log_to_file(message)
                print("1")
                # Apply the plcDataSnap7 function to each row of the DataFrame
                self.dfPlcdb[['Value', 'timestamp']] = self.dfPlcdb.apply(lambda row: pd.Series(snap7_plc.plcDataSnap7(self.plc, row['db_number'], row['data_type'], row['start_offset'], row['bit_offset'])), axis=1)
                # Assuming 'cursor' is your database cursor object
                # Create a list of tuples containing the values to be inserted  
                            
                values = [(row['timestamp'], row['Name'], row['data_type'], row['Value']) for _, row in self.dfPlcdb.iterrows()]                
                # Execute the query to insert multiple rows
                start = datetime.now()
                self.cursorWrite.executemany('''INSERT INTO plc_data (TimeStamp, Name, DataType, Value)
                                    VALUES (?, ?, ?, ?)''', values)
                self.conn.commit()
                end = datetime.now()
                # Inserting data to txt fife foe optmize the time
                # with open('ValuesData.txt', 'a') as file:  
                #     file.write(str(values) + '\n') 
                result = end - start
                print("insert indb difference time", result )

                


                self.local_conn = True


                            

                # Set column widths for better display
                

                #########Calculate 1st and last data timestamp difference################
                # Define the date strings with milliseconds and the format they follow
                end_time_str = self.dfPlcdb.loc[len(self.dfPlcdb)-1, 'timestamp']
                start_time_str = self.dfPlcdb.loc[0, 'timestamp']
                date_format = "%Y-%m-%d %H:%M:%S.%f"
                # Convert the strings to datetime objects
                start_time = datetime.strptime(start_time_str, date_format)
                end_time = datetime.strptime(end_time_str, date_format)
                
                
                
                # Calculate the time difference
                time_difference = end_time - start_time
                self.Total_seconds= str(time_difference.total_seconds())
                #print("Total seconds:", time_difference.total_seconds())
                message = 'Logging  - '  + str(timestamp) + ' -  Data fetching from PLC ' + 'in ' + self.Total_seconds + 'secs' 
                self.log_to_file(message)
                
        except Exception as e:
            # self.monitor_timer.stop()
            self.local_conn = False                        
            message = f"Error - {str(self.current_date)} - {e}"                        
            self.log_to_file(message)
            mail.send_email() 

    # def plcDataSnap7(self, db_number, data_type, start_offset, bit_offset):
    #     try:
    #         if data_type == 'BOOL':
    #             reading = self.plc.db_read(db_number, start_offset, 1)
    #             value = snap7.util.get_bool(reading, 0, bit_offset)
    #         elif data_type == 'REAL':
    #             reading = self.plc.db_read(db_number, start_offset, 4)
    #             value = round(struct.unpack('>f', reading)[0], 2)
    #             # reading = self.plc.db_read(db_number, start_offset, 4)
    #             # value = struct.unpack('>f', reading)[0]
    #         elif data_type == 'INT':
    #             reading = self.plc.db_read(db_number, start_offset, 2)
    #             value = struct.unpack('>h', reading)[0]
    #         elif data_type == 'DINT':  # Add support for double integer (4 bytes)
    #             reading = self.plc.db_read(db_number, start_offset, 4)
    #             value = struct.unpack('>i', reading)[0]
    #         else:
    #             print("Unsupported data type:", data_type)
    #             return None
            
    #         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    #         return value, timestamp  
    #     except Exception as e:
    #         message = f"Error - {str(self.current_date)} - {e}"                        
    #         self.log_to_file(message)
    #         #self.logField.append(f"Error : {e}")   

    # def read_trigger_status(self):
    #     try:
    #         # Replace with the actual logic to read the trigger status from the PLC
    #         db_number = 1  # Example DB number, replace with your actual DB number
    #         start_offset = 0  # Example start offset, replace with your actual start offset
    #         bit_offset = 0  # Example bit offset, replace with your actual bit offset
    #         trigger_reading = self.plc.db_read(db_number, start_offset, 1)
    #         trigger_status = snap7.util.get_bool(trigger_reading, 0, bit_offset)
    #         return trigger_status
    #     except Exception as e:
    #         message = f"Error reading trigger status - {e}"
    #         self.log_to_file(message)
    #         return False
 

    # def reset_trigger(self):
    #     try:
    #         # Replace with the actual logic to reset the trigger in the PLC
    #         db_number = 1  # Example DB number, replace with your actual DB number
    #         start_offset = 0  # Example start offset, replace with your actual start offset
    #         bit_offset = 0  # Example bit offset, replace with your actual bit offset
    #         data = bytearray(1)
    #         snap7.util.set_bool(data, 0, bit_offset, False)
    #         self.plc.db_write(db_number, start_offset, data)
    #         print("Trigger reset successfully.")
    #     except Exception as e:
    #         message = f"Error resetting trigger - {e}"
    #         self.log_to_file(message)
    def select_backup_path(self):
        root = Tk()
        root.withdraw()  # Hide the main window

        # # Prompt user to select backup file path
        backup_path = filedialog.asksaveasfilename(defaultextension=".bak",
                                                    filetypes=[("Backup files", "*.bak"), ("All files", "*.*")])
        # self.backup_path = "C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup\PLCDB2.bak"
        server_name = 'SURESHGOPI'
        # server_name = 'Localhost\SQLEXPRESS'
        database = 'PLCDB2'
        conn = self.conn
        cursorWrite = self.cursorWrite
        db_con.backup_database(conn,  database, cursorWrite, backup_path)
        message = 'File Backuped Successful'
        self.log_to_file(message)
#############################################              Graph                ###################################################################
    def graph(self):
        try:
            self.Ui.progressBar.show()
            layout = QDialog(self)
            vlayout = QVBoxLayout()
            layout.setWindowTitle("Plot Graph")
            self.button = QtWidgets.QPushButton('Plot', self)
            self.browser = QtWebEngineWidgets.QWebEngineView(self)

            
            vlayout.addWidget(self.button, alignment=QtCore.Qt.AlignHCenter)
            vlayout.addWidget(self.browser)

            # Enable the maximize button
            layout.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)
        

            df = self.df
            fig = graphs.plot_graph(df)
            self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

            layout.resize(1000,800)
            layout.setLayout(vlayout)
            layout.exec_()
            self.Ui.progressBar.hide()

        except Exception as e:
            print(f"Error: {e}")

    def barGraph(self):
            try:
                # self.Ui.verticalLayout_web.removeWidget(self)
                while self.Ui.verticalLayout_bar.count():
                    widget = self.Ui.verticalLayout_bar.takeAt(0).widget()
                    if widget is  None:
                        widget.deleteLater()
                
                self.browser = QWebEngineView(self.Ui.homePage)  # Create the QWebEngineView

                self.browser.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                self.browser.setMinimumSize(721, 471) 

                self.browser.setStyleSheet("color: #171725; background-color: #F7F8F9; font-size: 16px; font-family: Open Sans;")
               
                self.Ui.verticalLayout_bar.addWidget(self.browser)

                fig = graphs.show_bar(self.engineConRead)
                self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

            
            except Exception as e:
                print(f"Error: {e}")
    
    def speedGraph(self):
        try:
            # self.Ui.verticalLayout_web.removeWidget(self)
            while self.Ui.verticalLayout_web.count():
                widget = self.Ui.verticalLayout_web.takeAt(0).widget()
                if widget is None:
                    widget.deleteLater()
            
            self.browser = QWebEngineView(self.Ui.homePage)  # Create the QWebEngineView
            self.browser.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            self.browser.setMinimumSize(721, 471)
            self.browser.setStyleSheet("color: #171725; background-color: #F7F8F9; font-size: 16px; font-family: Open Sans;")
            
            self.Ui.verticalLayout_web.addWidget(self.browser)
            if self.local_connStatus == True:
                fig = graphs.show_speed(self.Total_seconds)



            self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

            

        # self.button.clicked.connect(self.show_graph)
        # self.resize(1000,800)
        # self.show_graph()
        # Set the URL to load if needed
        # self.browser.setUrl(QUrl("https://www.example.com")) 
        except Exception as e:
            print(f"Error: {e}")
   
###############################################        Logs              ##############################################################    
    def log_to_file(self, message): 
        # timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")  
        with open('log.txt', 'a') as file:  
            file.write( message + '\n')         
        self.logField.append(message)               

    def clear_logs(self):
        self.logField.clear()  # Clear the text editor
        with open('log.txt', 'w') as file:
            file.write('')  # Clear the log file
#################################################   Timers    #######################################################                 
    def timer_logging(self):
        self.monitor_timer = QTimer()
        self.monitor_timer.timeout.connect(self.timer1)
        print("Timer done : ",datetime.now())
        self.monitor_timer.start(15000)    

    def timer1 (self):
        if self.local_conn == False:                
            self.plcConnect() 
        elif self.local_connStatus == True:
            #self.run_logging()
            selected_columns = ['timestamp', 'Name', 'data_type', 'Value']
            self.df = self.dfPlcdb[selected_columns]
            self.model = PandasTableModel(self.df)
            self.Ui.liveTableDataView.setModel(self.model)

            self.Ui.liveTableDataView.setColumnWidth(0, 200)
            self.Ui.liveTableDataView.setColumnWidth(1, 200)
            self.Ui.liveTableDataView.setColumnWidth(2, 100)
            self.Ui.liveTableDataView.setColumnWidth(3, 100)

            self.thread_and_handle(self.run_logging)
            print("Logging done : ",datetime.now())
        else:
            print("true")
 
################################################   Import excel #########################################################################
    def open_excel_file(self):
        # Open file dialog to select Excel file
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel files (*.xlsx *.xls)")
        if file_name:
            # Read data from Excel into DataFrame
            try:
                self.dfPlcExcel = pd.read_excel(file_name)
                # self.thread_and_handle(self.insert_data_into_mysql())
                # cursorWrite = self.cursorWrite
                
                db_con.insert_data_into_mysql(self.cursorWrite,self.dfPlcExcel)
                #self.logImp.append("Data inserted into MySQL table successfully.")
                self.Ui.logImp.append("PLC Data information successfully updated.")
                self.dfPlcdb= db_con.dfPlc(self.engineConRead, self.softwaretype)

            except Exception as e:
                self.Ui.logImp.append(f"Error reading Excel file: {e}")

class PandasTableModel(QAbstractTableModel):
    def __init__(self, data):
        super(PandasTableModel, self).__init__()    
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            elif orientation == Qt.Vertical:
                return str(section + 1)
        return None

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = PLCDataLogger()
    Mainwindow.show()
    sys.exit(app.exec_())
  