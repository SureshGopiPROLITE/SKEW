import pyodbc
from sqlalchemy import create_engine, text
import pandas as pd
import datetime
from datetime import datetime, timedelta

def dbConnection():
    try:
        conn = pyodbc.connect(
            'DRIVER=SQL Server;'
            'SERVER=SURESHGOPI;'
            'DATABASE=PLCDB2;'
        )
        cursorRead = conn.cursor()
        cursorWrite = conn.cursor()
        engine = create_engine('mssql+pyodbc://SURESHGOPI/PLCDB2?driver=SQL+Server')
        engineConRead = engine.connect()
        engineConWrite = engine.connect()



    except Exception as e:
        print("Error connecting to database:", e)
        raise
    return cursorRead, cursorWrite, engineConRead, engineConWrite, conn

def dfPlc(engineConRead, softwaretype):        
    try:
        print("Software Type:", softwaretype)
        if softwaretype  == 0 or softwaretype  == 1:
            print("Software Type:", softwaretype)
            # Retrieve data from MySQL table after insertion
            select_query = text("SELECT  * FROM Data")
            # Load data into a DataFrame
            dfdemo = pd.read_sql_query(select_query, engineConRead)

            dfPlcdb = dfdemo.head(50)
            dfPlcdb['db_number'] = pd.to_numeric(dfPlcdb['db_number'], errors='ignore', downcast='integer')
            dfPlcdb['start_offset'] = pd.to_numeric(dfPlcdb['start_offset'], errors='ignore', downcast='integer')
            dfPlcdb['bit_offset'] = pd.to_numeric(dfPlcdb['bit_offset'], errors='ignore', downcast='integer')
            print(dfPlcdb)
            return dfPlcdb
        else:
            select_query = text("SELECT  * FROM Data")
            dfPlcdb = pd.read_sql_query(select_query, engineConRead)
            dfPlcdb['db_number'] = pd.to_numeric(dfPlcdb['db_number'], errors='ignore', downcast='integer')
            dfPlcdb['start_offset'] = pd.to_numeric(dfPlcdb['start_offset'], errors='ignore', downcast='integer')
            dfPlcdb['bit_offset'] = pd.to_numeric(dfPlcdb['bit_offset'], errors='ignore', downcast='integer')
            print(dfPlcdb)
            return dfPlcdb
        
    except Exception as e:
        return e
    # print(dfPlcdb)

def archive_old_data(cursorWrite):
    try:
        # Calculate cutoff date for archival (30 days ago)
        cutoff_date = datetime.now() - timedelta(days=30)
        cutoff_date_str = cutoff_date.strftime('%Y-%m-%d')
        
        # Move records older than cutoff_date from plc_data to plc_data_archive
        cursorWrite.execute(f'''INSERT INTO plc_data_archive (TimeStamp, Name, DataType, Value)
                                SELECT TimeStamp, Name, DataType, Value
                                FROM plc_data
                                WHERE TimeStamp < ?''', (cutoff_date_str,))
        
        # Delete records older than cutoff_date from plc_data
        cursorWrite.execute(f'''DELETE FROM plc_data
                                WHERE TimeStamp < ?''', (cutoff_date_str,))
        
        # Commit changes
        cursorWrite.commit()
    
    except Exception as e:
        print(f"Error archiving data: {e}")
   
        # Handle error as needed

def show_data(hours, from_time, to_time, engineConRead):
    try:
        if hours == "Custom":                
            print("Time : ", from_time, to_time)
            
            from_time_dt = datetime.fromisoformat(from_time)
            to_time_dt = datetime.fromisoformat(to_time)

            # Calculate the difference
            date_diff = to_time_dt - from_time_dt
            print("Date Difference:", date_diff)    
            
            if date_diff.days >= 30:
                    
                # Query database for data between specified timestamps from both tables
                query = f"""
                SELECT * FROM plc_data
                WHERE TimeStamp BETWEEN '{from_time}' AND '{to_time}'
                
                UNION ALL
                
                    SELECT * FROM plc_data_archive
                WHERE TimeStamp BETWEEN '{from_time}' AND '{to_time}'
                ORDER BY TimeStamp ASC; 
                """
                df = pd.read_sql_query(query, engineConRead)
            else:
                print(date_diff)
                # Query database for data between specified timestamps   
                query = f"""SELECT * FROM plc_data WHERE TimeStamp BETWEEN '{from_time}' AND '{to_time}'"""
                df = pd.read_sql_query(query, engineConRead)
                

        elif hours in ["1 Hr", "4 Hr", "8 Hr", "12 Hr", "24 Hr"]:
            # Determine the hour range for predefined selections
            if hours == "1 Hr":
                hours_ago = 1
            elif hours == "4 Hr":
                hours_ago = 4
            elif hours == "8 Hr":
                hours_ago = 8
            elif hours == "12 Hr":
                hours_ago = 12
            elif hours == "24 Hr":
                hours_ago = 24
            
            # Construct the SQL query based on the selected hours range
            sql = f"""
                SELECT *
                FROM plc_data
                WHERE TimeStamp >= DATEADD(HOUR, -{hours_ago}, GETDATE())
                ORDER BY TimeStamp ASC; 
                """
            df = pd.read_sql_query(sql, engineConRead)
            
        else:
            print("Select a valid time range")

        # Set up the DataFrame and model for display
        return df

    except Exception as e:
        print(f"An error occurred: {e}")

def export_data(engineConRead, from_time, to_time):
    try:           
        query = "SELECT * FROM plc_data WHERE TimeStamp BETWEEN ? AND ?"
        df = pd.read_sql_query(query, engineConRead, params=(from_time, to_time))
        #  # Check if DataFrame is available
        return df
    except Exception as e:
        print(f"Error archiving data: {e}")

def backup_database(conn, database, cursorWrite, backup_path):
    try:
        # Get the backup path selected by the user
        conn.autocommit = True

        # # Define the SQL backup command
        backup_command = f'BACKUP DATABASE [{database}] TO DISK = \'{backup_path}\''

    
        # Execute the backup command
        cursorWrite.execute(backup_command)

        print(f"Backup of database '{database}' completed successfully.")
       
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
            # Close cursor and connection
            cursorWrite.commit()
            conn.commit()
 
def insert_data_into_mysql(cursor, dfPlcExcel):
    try:
        # Truncate the table to clear all existing data
        truncate_query = "TRUNCATE TABLE Data"
        cursor.execute(truncate_query)

        # Dynamically generate CREATE TABLE query based on DataFrame columns
        columns = ', '.join([f"{col} VARCHAR(255)" for col in dfPlcExcel.columns])
        create_table_query = f"""
            IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Data')
            BEGIN
                CREATE TABLE Data ({columns})
            END
        """
        cursor.execute(create_table_query)

        # Insert data into the table
        for index, row in dfPlcExcel.iterrows():
            # Dynamically generate INSERT INTO query based on DataFrame columns
            placeholders = ', '.join(['?' for _ in dfPlcExcel.columns])  # Using ? as parameter placeholder
            columns = ', '.join(dfPlcExcel.columns)
            sql = f"INSERT INTO Data ({columns}) VALUES ({placeholders})"
            # Pass values as a tuple directly to execute
            cursor.execute(sql, tuple(row))
        # Commit changes            
        cursor.commit()

    except Exception as e:
        print(f"Error occurred: {str(e)}")
