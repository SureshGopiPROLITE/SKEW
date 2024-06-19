import snap7
import struct
import pandas as pd
from sqlalchemy import create_engine, text
import datetime
from datetime import datetime, timedelta                 
      


def snap7Connect(plcIP, rack, slot):
    try:
        print(plcIP, rack, slot)
        plc = snap7.client.Client()
        plc.connect(plcIP, rack, slot)
        return plc
    except Exception as e:
        print(f"Error updating license: {e}")

def plcDataSnap7(plc, db_number, data_type, start_offset, bit_offset):
    try:
        if data_type == 'BOOL':
            reading = plc.db_read(db_number, start_offset, 1)
            value = snap7.util.get_bool(reading, 0, bit_offset)
        elif data_type == 'REAL':
            reading = plc.db_read(db_number, start_offset, 4)
            value = round(struct.unpack('>f', reading)[0], 2)
            # reading = plc.db_read(db_number, start_offset, 4)
            # value = struct.unpack('>f', reading)[0]
        elif data_type == 'INT':
            reading = plc.db_read(db_number, start_offset, 2)
            value = struct.unpack('>h', reading)[0]
        elif data_type == 'DINT':  # Add support for double integer (4 bytes)
            reading = plc.db_read(db_number, start_offset, 4)
            value = struct.unpack('>i', reading)[0]
        else:
            print("Unsupported data type:", data_type)
            return None
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

        return value, timestamp  
    except Exception as e:
        print(f"Error updating license: {e}") 

# def snap7Read(plc, df)