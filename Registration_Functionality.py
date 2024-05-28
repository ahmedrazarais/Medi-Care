# importing mysql and from config file details for connection
import mysql.connector

from Database_Creation import Database_for_Hospital

# class for signup and inherits woith database class

class Signup(Database_for_Hospital):
    def __init__(self):
        self.type=""   # inital ait empty then what user wants change to it
        super().__init__()  # calling parent constructor



    
    # method to insert accounts data in table
    def insert_data_in_accounts(self,id,name,gmail,user_id,password,acc_type):
        try:
            # query to insert data in table
            insert_query="INSERT INTO hospital.accounts_hosp VALUES(%s,%s,%s,%s,%s,%s)"

            # exceute that query
            self.cursor.execute(insert_query,(id,name,gmail,user_id,password,acc_type))

            # commit the change
            self.conn.commit()
            print("Data Inserted Successfully.Your Account Created Successfully.\n")

        except mysql.connector.Error as e:
            print(f"Error in insertion of data {e}.\n")



    # method to fetch data from accounts_hosp table
    def fetch_data_from_accounts(self):
        try:
            # query to fetch data
            fetch_query="SELECT * FROM hospital.accounts_hosp"

            # exceute that query
            self.cursor.execute(fetch_query)

            # get all data from table
            data=self.cursor.fetchall()

            # return data
            return data

        except mysql.connector.Error as e:
            print(f"Error in fetching data from table {e}")
    

    # mehtod to take id (primary key) input
    def id_input(self):
        data=self.fetch_data_from_accounts() # calling mehtod to get data list from table
        # taking id input
        while True:
            try:
                id_input=int(input("Enter Id for Further Procedure (enter 0 to back):"))
                if id_input==0:   # if want to go back
                    print("Return To previous Options..\n")
                    return
                
                if id_input<=0:
                    print("Id Must not be zero or less than zero\n")

                # check id must not be repeated beacuse of primary key
                if data:
                    found = False
                    for row in data:
                        if id_input==row[0]:  # If id matches
                            found=True
                            break
                    if found:
                        print("Please Select another Id This id already exists.\n")
                    # if id not matches
                    else:
                        print("Id assign successfully\n")
                        return id_input
                # for initial when no data enter
                else:
                    print("Id assign successfully\n")
                    return id_input

            # if getting id rather than in number
            except ValueError:
                print("\nPlease Enter In Digit Id must be in digit\n")



    # method for name input
    def get_name(self):
        # get name input in loop
        while True:
            name=input(f"Dear {self.type} Please Enter Your Name (enter 0 to back):").strip()

            if name=="0":
                return

            # check if name is empty
            if name=="":
                print("\nName can't be empty.Please Enter Your Name\n")

            # check if name contain only aplhabets and spaces
            elif not name.replace(" ","").isalpha():
                print("\nName can only contain alphabets and spaces.Please Enter Correct Name\n")

            else:
                return name
            

    # method for gmail input
    def get_gmail(self):
        # get gmail input in loop
        while True:
            print()
            gmail=input(f"Dear {self.type} Please Enter Your Gmail (enter 0 to back):").strip()

            if gmail=="0":
                return

            # check if gmail is empty
            if gmail=="":
                print("\nGmail can't be empty.Please Enter Your Gmail\n")
            # check @ not in starts and gmail ended with @gmail.com
            elif not gmail.endswith("@gmail.com"):
                print("\nGmail must end with @gmail.com.Please Enter Correct Gmail\n")

            # check if gmail contain @
            elif "@" not in gmail:
                print("\nGmail must contain @.Please Enter Correct Gmail\n")

            else:
                return gmail
            
    # method for user_id input ALSO check if user_id already exist
    def get_user_id(self):
        # call fetch data method
        data = self.fetch_data_from_accounts()

        # normalize existing user IDs to lower case for case-insensitive comparison
        existing_user_ids = {item[3].lower() for item in data} if data else set()

        # get user_id input in loop
        while True:
            print()
            user_id = input(f"Dear {self.type}, please enter your User_id (enter 0 to back):").strip()

            if user_id == "0":
                return

            # lower case user_id
            user_id_lower = user_id.lower()

            # check if user_id is empty
            if user_id == "":
                print("\nUser_id can't be empty. Please enter your User_id\n")
                continue

            # check if user_id already exists (case-insensitive)
            if user_id_lower in existing_user_ids:
                print("\nUser_id already exists. Please enter another User_id\n")
            else:
                return user_id
                
    # method for password input
    def get_password(self):
        # get password input in loop
        while True:
            print()
            password=input(f"Dear {self.type} Please Enter Your Password:").strip()

            # check if password is empty
            if password=="":
                print("\nPassword can't be empty.Please Enter Your Password\n")

            # check if password contain atleast 8 characters
            elif len(password)<8:
                print("\nPassword must contain atleast 8 characters.Please Enter Correct Password\n")

            else:
                print()
                return password
            

    
    # make table in which make table name as self.doc_table with columns id patient name disease appointment date appointment status medicines you suggested
    def create_table_for_doctors_appointments(self,doc_name):
        # create table in database hospital with try except to avoid conflicts
        try:
            self.cursor.execute("USE hospital")
            tb_query=f"""CREATE TABLE IF NOT EXISTS {doc_name} (
            id INT ,
            patient_name VARCHAR (50),
            disease VARCHAR (50),
            appointment_date VARCHAR (30),
            appointment_status VARCHAR (50),
            medicines_you_suggested VARCHAR (50),
            patient_user_id VARCHAR (50)
            )"""

            # exceute that query
            self.cursor.execute(tb_query)

            # commit the change
            self.conn.commit()
            
            print("Table for doctor created successfully.\n")

        except mysql.connector.Error as e:
            print(f"Error in creation of table as {e}")


    # method to create table in hospital,id,doctor name,disease,appointment date,appointment status,medicines you got
    def create_table_for_patients_appointments(self,pat_name):
        # create in hospital database with try except to avoid conflicts
        try:
            
            self.cursor.execute("USE hospital")
            tb_query=f"""CREATE TABLE IF NOT EXISTS {pat_name} (
            id INT ,
            doctor_name VARCHAR (50),
            disease VARCHAR (50),
            appointment_date VARCHAR (50),
            appointment_status VARCHAR (50),
            medicines_you_got VARCHAR (50)
            )"""

            # exceute that query
            self.cursor.execute(tb_query)

            # commit the change
            self.conn.commit()
            
            print("Table for patients created successfully.\n")

        except mysql.connector.Error as e:
            print(f"Error in creation of table as {e}")



        
            
  


    # method to take type input
    def type_account(self):
        print("\tWelcome To signup Area.\n")

        # loop to stuck till user want to exit
        while True:
            # options for user
            print("\tSelect Your Account Type.\n")
            print("\t1.Create Account As Doctor.")
            print("\t2.Create Account As User/Patient.")
            print("\t3.Back From Registration Area.\n")
            
            # taking user choice
            user_choice=input("Enter Your Registartion Choice:").strip()

            if user_choice=="1":
                # change to doctor type
                self.type="doctor"
                print("Now you can create acccount As Doctor\n")
                # call respective methods
                id=self.id_input()
                if id:
                  name=self.get_name()

                  if name:        # check if name is entered
                    gmail=self.get_gmail()

                    # check if gmail is entered
                    if gmail:
                        # check if user_id is entered
                        user_id=self.get_user_id()

                        if user_id:

                            password=self.get_password()

                            if password:

                                self.insert_data_in_accounts(id,name,gmail,user_id,password,self.type)
                                self.create_table_for_doctors_appointments(user_id)
                                print("Account Created Successfully.\n")

                                break

                            else:
                                print("Password Not Entered Correctly.Please Enter Correct Password\n")
                        else:
                            print("User_id Not Entered Correctly.Please Enter Correct User_id\n")
                    else:
                        print("Gmail Not Entered Correctly.Please Enter Correct Gmail\n")
                else:
                    print("Name Not Entered Correctly.Please Enter Correct Name\n")


            # FOR patients accounts        
            elif user_choice=="2":
                # change to patient type
                self.type="patient"
                print("Now you can create acccount As Patient\n")
                # call respective methods
                id=self.id_input()
                if id:
                  name=self.get_name()
                  if name:
                    gmail=self.get_gmail()
                    if gmail:
                        user_id=self.get_user_id()
                        if user_id:
                            password=self.get_password()
                            if password:
                                self.insert_data_in_accounts(id,name,gmail,user_id,password,self.type)
                                self.create_table_for_patients_appointments(user_id)
                                print("Account Created Successfully.\n")
                                break
                            else:
                                print("Password Not Entered Correctly.Please Enter Correct Password\n")
                        else:
                            print("User_id Not Entered Correctly.Please Enter Correct User_id\n")
                    else:
                        print("Gmail Not Entered Correctly.Please Enter Correct Gmail\n")
                else:
                    print("Name Not Entered Correctly.Please Enter Correct Name\n")

           
           # Exit Option
            elif user_choice=="3":
               # exit option
               print("Back From Registration Area...\n")
               break

            # if invalid choice
            else:
                print("Invalid Choice Get In Regisration.Please Select Correct One\n")

