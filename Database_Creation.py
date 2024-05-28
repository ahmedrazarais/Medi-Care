
# importing mysql and from config file details for connection
import mysql.connector
from config import db_host,db_password,db_user
from Database_Connection import Connection





# class for making database and inhertis it from connection class
class Database_for_Hospital(Connection):
    def __init__(self):
        super().__init__()   # calling parent constructor
    


    
    # method to craete database name hospital
    def create_database(self):
        try:
            db_query="CREATE DATABASE IF NOT EXISTS hospital"

            # exceute that query
            self.cursor.execute(db_query)

            # commit the change
            self.conn.commit()
       
            
        except mysql.connector.Error as e:
            print(f"Error in creation of database {e}\n")

    
    # method to create table of accounts for doctors and patients in hospital database 
    def create_table_for_accounts_hospital(self):
        # use try except to avoid conflicts
        try:
            self.cursor.execute("USE hospital")
            tb_query="""CREATE TABLE IF NOT EXISTS accounts_hosp (
            id INT PRIMARY KEY,
            name VARCHAR (50),
            gmail VARCHAR (50),
            user_id VARCHAR (60),
            password VARCHAR (50),
            acc_type VARCHAR (50)
            )"""

            # exceute that query
            self.cursor.execute(tb_query)

            # commit the change
            self.conn.commit()
            
           

        except mysql.connector.Error as e:
            print(f"Error in creation of table as {e}")