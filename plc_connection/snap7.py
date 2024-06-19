import snap7

import pandas as pd
from sqlalchemy import create_engine, text
                 
      

def plcConnect(self):
    try:
        self.plcIP = self.Ui.inpIp.text()
        self.rackandslot = self.Ui.inpRackSlot.text()
        # rack, slot = map(int, self.rackandslot.split(','))
        print(self.plcIP)
        query = text('SELECT * FROM Info_DB')
        self.dfInfo = pd.read_sql_query(query, self.con)
        if self.plcIP == "" or self.rackandslot == "":
            self.rackandslot = self.dfInfo.loc[5, 'Info']
            rack, slot = map(int, self.rackandslot.split(','))
            
            self.plcIP = self.dfInfo.loc[0, 'Info']               
            self.current_date = datetime.now()
            self.plc = snap7.client.Client()
            # self.plc.connect(self.plcIP, 0, 1)
            self.plc.connect(self.plcIP, rack, slot)
            print("PLC Connected" , self.plc)
            print("DB Connected", self.cursor)
            print("DB Connected", self.con)
            #self.log.append('PLC is connected'  +  str(self.current_date))
            message = 'Info  - '  + str(self.current_date) + ' -  PLC is connected ' 
            self.log.append(message)
            self.log_to_file(message)
            self.local_connStatus = True
            self.dfPlc()
            # self.insert_data_from_notepad()
            self.run_logging()
        elif self.plcIP:
            query = "UPDATE Info_DB SET Info = ? WHERE CAST(Particulars AS NVARCHAR(MAX)) = ?"
            self.cursor.execute(query, (self.rackandslot, "Info"))
            rack, slot = map(int, self.rackandslot.split(','))

            query = "UPDATE Info_DB SET Info = ? WHERE CAST(Particulars AS NVARCHAR(MAX)) = ?"
            # Execute the query with parameters
            self.cursor.execute(query, (self.plcIP, "Plc_IP"))
            self.cursor.commit()
            self.current_date = datetime.now()
            self.plc = snap7.client.Client()
            # self.plc.connect(self.plcIP, 0, 1)
            self.plc.connect(self.plcIP, rack, slot)
            print("PLC Connected" , self.plc)
            print("DB Connected", self.cursor)
            print("DB Connected", self.conn)


            
            
            message = 'Info  - '  + str(self.current_date) + ' -  PLC is connected ' 
            self.log.append(message)
            self.log_to_file(message)
            self.local_connStatus = True
            self.dfPlc()
            self.run_logging()

        else:
            self.log.append(f'PLC IP: {e}') 
            print("PLC IP address is not provided.")
            # You might want to inform the user or take appropriate action here

        
    except Exception as e:
        self.log.append(f'PLC is not connected: {e}') 
        print("Not connecting", e)
        self.logField.append(f"Error : {e}")
        self.monitor_timer.stop()
        self.local_connStatus = False
        self.send_email()
    return self.local_connStatus


        
    return self.local_connStatus


def snap7Connect(plcIP, rack, slot):
    try:
        print(plcIP, rack, slot)
        plc = snap7.client.Client()
        plc.connect(plcIP, rack, slot)
        return plc
    except Exception as e:
        print(f"Error updating license: {e}")

# def snap7Read(plc, df)