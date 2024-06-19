
# from PyQt5.QtCore import QTimer

from datetime import datetime, timedelta
import time


# import pandas

from database import db_con as db_con
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
import sys

# from plc_data_ui import Ui_MainWindow
from main import PLCDataLogger as PLCDataLogger 


        
def timer_logging():
    monitor_timer = QTimer()
    monitor_timer.timeout.connect(PLCDataLogger.timer1)
    monitor_timer.start(5000)  
    print("Timer done : ",datetime.now())      



def timerTable():
    monitor_timer = QTimer()
    monitor_timer.timeout.connect(db_con.archive_old_data)
    monitor_timer.start(86400000)  

def onehr_timer(fun):
    PLCDataLogger.speedGraph()
    monitor_timer = QTimer()
    monitor_timer.timeout.connect(fun)
    monitor_timer.start(36,00,000)

# def timerDataInsert():
#     monitor_timer = QTimer()
#     monitor_timer.timeout.connect(insert_data_from_notepad)
#     monitor_timer.start(10000)

