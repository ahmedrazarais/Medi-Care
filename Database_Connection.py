


# importing mysql and from config file details for connection
import mysql.connector
from config import db_host,db_password,db_user


# class for making connection of database
class Connection:
    def __init__(self):
        try:    # use try except to avoid program from crush
            self.conn=mysql.connector.connect(
                host=db_host,
                password=db_password,
                user=db_user,        
        )   
            # making pointer for use later 
            self.cursor=self.conn.cursor()
            return True


        # if getting error
        except mysql.connector.Error as e:
            print(f"ERROR: In Connection {e}.")
            print("Please check your database details in config file and try again.\n")
            exit()

    # methofd for closing connection
    def close_connection(self):
           try:    # use try excpet to avoid conficts

            # checking if cursor assigned then close it
            if self.cursor:
                self.cursor.close()
                print("Cursor closed.\n")

            # if connection there then close it
            if self.conn.is_connected():
                self.conn.close()
                print("Connection closed.\n")

           # if getting error in closing connection
           except mysql.connector.Error as e:
              print(f"ERROR: In closing connection {e}.")
