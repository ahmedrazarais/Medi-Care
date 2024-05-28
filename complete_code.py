# importing mysql and from config file details for connection
import mysql.connector
from config import db_host,db_password,db_user
import random
import os

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
            print("Connection Successfull.\n")

        # if getting error
        except mysql.connector.Error as e:
            print(f"ERROR: In Connection {e}.")

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
            print('Database created Successfull')
            
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
            
            print("Table for accounts created successfully.\n")

        except mysql.connector.Error as e:
            print(f"Error in creation of table as {e}")


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




# class for login and inherits with signup class for multilevel inheritance
# class for login and inherits with signup class for multilevel inheritance
class Login(Signup):
    def __init__(self):
        self.login_type = ""  # Initialize login type
        self.doc_table = ""
        self.patient_table = ""
        super().__init__()  # Call parent constructor

    # Method for the login process
    def login_process(self):
        print("\tWelcome To Login Area.\n")

        while True:
            print("\tSelect Your Account Type.\n")
            print("\t1.Login As Doctor.")
            print("\t2.Login As User/Patient.")
            print("\t3.Back From Login Area.\n")

            user_choice = input("Enter Your Login Choice:").strip()

            if user_choice == "1":
                 self.login_type = "doctor"
                 user_id = self.get_id_for_login()
                 if user_id:        
                    self.doctor_table = user_id
                   
                    
                    # Initialize Doctors class with the Doctor's table name and Patient's table name
                    d = Doctors(self.doctor_table, self.patient_table)
                    d.main_page_doctors()  # Redirect to Doctor's main page
                    break

            elif user_choice == "2":
                self.login_type = "patient"
                user_id = self.get_id_for_login()
                if user_id:        
                    self.patient_table = user_id
                   
                    
                    # Initialize Patients class with the patient's table name
                    p = Patients(self.patient_table)
                    p.main_page_patients()  # Redirect to patient's main page
                    break

            elif user_choice == "3":
                print("Back From Login Area...\n")
                break

            else:
                print("Invalid Choice. Please Select Correct One\n")

    # Method to validate user credentials and get user_id for login
    def get_id_for_login(self):
        data = self.fetch_data_from_accounts()

        while True:
            user_id = input(f"Dear {self.login_type}, Please Enter Your User_id (enter 0 to back):").strip()

            if user_id == "0":
                return False

            found = False
            for row in data:
                if user_id == row[3] and self.login_type == row[5]:
                    found = True
                   
                    break

            if found:
                while True:
                    password = input(f"Dear {self.login_type}, Please Enter Your Password (enter 0 to back):").strip()

                    if password == "0":
                        return False

                    for row in data:
                        if password == row[4]:
                            print("\nWait for a while..")
                            print("Login Successful\n")
                            
                            return user_id
                    print("Password Not Matched. Please Enter Correct Password\n")
            else:
                print("User_id Not Found. Please Enter Correct User_id\n")
                continue

  
      






# class for patients inherits with Login class
class Patients(Login):
    def __init__(self,patient_table):
        self.table_accounts=patient_table    # chenge it it with patient name
        # table name for doctor initial empty
        self.doc_table=""
        self.doc_list=[]   # empty fill it with doc names
        super().__init__()      # calling parent constructor


    # main page for patients 
    def main_page_patients(self):
        print("\tWelcome In Medi-Care\n\n")

        # loop to stuck him till he want to go back
        while True:
            # Display options for patients
            print("\t1.See Your Profile.")
            print("\t2.View All Doctors Avaliable in Medi-Care.")
            print("\t3.Set Your Appointment For Checkup.")
            print("\t4.Update Your Profile.")
            print("\t5.See Your Appointments.")
            print("\t6.Cancel The Appointment.")
            print("\t7.Back From MediCare Patients Hub.\n\n")
            

            # taking patients chouce
            pat_choice=input("Dear Patient Enter Your Choice:").strip()

            # handling choice and calling respective methods
            if pat_choice=="1":
                self.view_profile_patients()  # call profile method

            elif pat_choice=="2":
                self.display_doctors_to_patients()   # call method of display doctors

            elif pat_choice=="3":
                self.set_appoitments()   # call method to set appointments

            elif pat_choice=="4":
                self.update_profile_patients()   # call method to update profile
            
            elif pat_choice=="5":
                self.display_appointments_patients()   # call method to display appointments

            elif pat_choice=="6":
                self.cancel_appointment()   # call method to cancel appointment

            # exit option for patient
            elif pat_choice=="7":
                print("Back From MediCare Patients Hub..")
                return 
            
            # Invalid choice
            else:
                print("Invalid Choice.Please Enter Correct Choice\n\n")    
    

    # method to filter doctor names and gmails from list
    def get_doc_names(self):
        self.doc_list=[]
        # calling method from signup class of fetch data of accounts
        data=self.fetch_data_from_accounts()
       
        # iterate and check for condition
        for item in data:
            if item[5]=="doctor":
                # also add here cehck that user id not repated mean in doc list check if id not in doc list
                if item[3] not in self.doc_list:
                   self.doc_list.append((item[0],item[1],item[2],item[5]))
        
        return self.doc_list
    

    # method to display all doctors to patients
    def display_doctors_to_patients(self):
        # call method get doctors to print in format style
        names=self.get_doc_names()

       # checking if no doctors have registered yet
        if not names:
            print("Something went wrong. Sorry for the inconvenience. No doctors are available at Medicare right now!\n\n")
            return

        # iterate over the list to print doctor details
        print("\t\tMedi-Care-Doctor's Details.\n\n")
        print("{:<10} {:<20} {:<30} {:<15}".format("Id", "Doctor-Name", "Doctor's-Gmail", "Profession"))
        print("-" * 80)

        for details in names:
            print(f"{details[0]:<10} {details[1]:<20} {details[2]:<30} {details[3]:<15}")

        print()


    # method to insert data in self.doc_table which is doctor's table
    def insert_data_in_doctors_appointments_table(self,pat_id,pat_name,disease,appointment_date,appointment_status,medicines_you_suggested,patient_user_id):
        try:
            # query to insert data in table
            insert_query=f"INSERT INTO hospital.{self.doc_table} VALUES(%s,%s,%s,%s,%s,%s,%s)"

            # exceute that query
            self.cursor.execute(insert_query,(pat_id,pat_name,disease,appointment_date,appointment_status,medicines_you_suggested,self.table_accounts))

            # commit the change
            self.conn.commit()
            print("Data Inserted Successfully.\n")

        except mysql.connector.Error as e:
            print(f"Error in insertion of data {e}.\n")


    

    # Method to insert data in self.account_table
    def insert_data_in_appointments_patients_table(self,doc_id,doc_name,disease,appointment_date,appointment_status,medicines_you_got):
        try:
            # query to insert data in table
            insert_query=f"INSERT INTO hospital.{self.table_accounts} VALUES(%s,%s,%s,%s,%s,%s)"

            # exceute that query
            self.cursor.execute(insert_query,(doc_id,doc_name,disease,appointment_date,appointment_status,medicines_you_got))

            # commit the change
            self.conn.commit()
            print("Data Inserted Successfully.\n")

        except mysql.connector.Error as e:
            print(f"Error in insertion of data {e}.\n")
    

    # method to cancel the appointment only if appointment status is pending otherwise not
    def cancel_appointment(self):
        # query to fetch data from patients table
        fetch_query=f"SELECT * FROM hospital.{self.table_accounts}"
        self.cursor.execute(fetch_query)
        data=self.cursor.fetchall()

                # Check if data is there
        if data:
            print("\t\tYour Appointments Details\n\n")
            print("{:<15} {:<20} {:<15} {:<20} {:<20} {:<20}".format(
                "Checkup-Id", "Doctor-Name", "Disease", "Appointment-Date", "Appointment-Status", "Medicines-You-Got"))
            print("-" * 110)
            for item in data:
                print("{:<15} {:<20} {:<15} {:<20} {:<20} {:<20}".format(
                    item[0], item[1], item[2], item[3], item[4], item[5]))
            print()
        else:
            print("\nNo Appointments Yet.\n")
            return

        # taking input of checkup id
        while True:
           
            try:
                checkup_id=int(input("Enter Checkup Id You Want to Cancel (enter 0 to back):"))
                if checkup_id==0:
                    return
                # check if checkup id is in data
                for item in data:
                    # check if checkup id is in data
                    if item[0]==checkup_id:
                        # check if appointment status is pending
                        if item[4]=="Pending":
                      

                            self.cursor.execute("USE HOSPITAL")
                            
                           
                            # now check in hospital database that if checkup id is found in any table then get that table name and delete that row
                            self.cursor.execute("SHOW TABLES")
                            tables=self.cursor.fetchall()
                            for table in tables:
                                table_name=table[0]
                                self.cursor.execute(f"SELECT * FROM hospital.{table_name}")
                                data=self.cursor.fetchall()
                                for row in data:
                                    if row[0]==checkup_id:
                                        delete_query=f"DELETE FROM hospital.{table_name} WHERE id={checkup_id}"
                                        self.cursor.execute(delete_query)
                                        self.conn.commit()
                                        break

                            

                             # Delete appointment from appointments_patients table
                            delete_query_patient = f"DELETE FROM {self.table_accounts} WHERE id={checkup_id}"
                            self.cursor.execute(delete_query_patient)
                            self.conn.commit()

                            

                         
                            print("\nAppointment Cancelled Successfully.\n")
                            return
                        
                        # if appointment status is not pending
                        else:
                            print("\nAppointment Status is not Pending.You Can't Cancel Appointment\n")
                            return
                # if checkup id not found
                print("\nCheckup Id Not Found.Please Enter Correct Checkup Id\n")
            
            # if getting checkup id in other than digits
            except ValueError:
                print("Please Enter In Digits\n")

  
    # method to give options to patients to update profile
    def update_profile_patients(self):
        print("\t\tUpdate Your Profile\n\n")
        while True:
             # call view profile method to show profile
            self.view_profile_patients()

            # Display options for patients
            print("\t1.Update Your Name.")
            print("\t2.Update Your Gmail.")
            print("\t3.Update Your Password.")
            print("\t4.Back From Update Profile.\n")
            
           

            # taking patients choice
            pat_choice=input("Dear Patient Enter Your Choice For Updation:").strip()

            # handling choice and calling respective methods
            if pat_choice=="1":
                # check if name is updated

                name=self.get_name()  # call method to update name
                if name:
                    # update in accounts table where user id is equal to patient table
                    update_query=f"UPDATE hospital.accounts_hosp SET name='{name}' WHERE user_id='{self.table_accounts}'"
                    self.cursor.execute(update_query)   # execute that query
                    self.conn.commit()  # commit the change
                    print("\nName Updated Successfully.\n")

            elif pat_choice=="2":
                gmail=self.get_gmail()   # call method to update gmail
                if gmail:
                    # update in accounts table where user id is equal to patient table
                    update_query=f"UPDATE hospital.accounts_hosp SET gmail='{gmail}' WHERE user_id='{self.table_accounts}'"
                    self.cursor.execute(update_query)   # execute that query
                    self.conn.commit()  # commit the change
                    print("\nGmail Updated Successfully.\n")


         

            elif pat_choice=="3":
                password=self.get_password()   # call method to update password
                if password:
                    # update in accounts table where user id is equal to patient table
                    update_query=f"UPDATE hospital.accounts_hosp SET password='{password}' WHERE user_id='{self.table_accounts}'"
                    self.cursor.execute(update_query)     # execute that query
                    self.conn.commit()    # commit the change
                    print("\nPassword Updated Successfully.\n")

             
            # exit option for patient from update profile
            elif pat_choice=="4":
                print("Back From Update Profile..")  # exit option
                return

            # Invalid choice
            else:
                print("\nInvalid Choice.Please Enter Correct Choice\n\n")

    # method for patient to see profile
    def view_profile_patients(self):
        # calling fetch data method to get data
        data=self.fetch_data_from_accounts()
        
        print("\t\tProfile's Details\n")
        print("{:<10} {:<20} {:<30} {:<15} {:<15}".format("Id", "Patient-Name", "Gmail", "User-Id", "Password"))
        print("-" * 100)
        # Iterate over data
        for item in data:
            # Check if user id is equal to patient's table
            if item[3] == self.table_accounts:
                print("{:<10} {:<20} {:<30} {:<15} {:<15}".format(item[0], item[1], item[2], item[3], item[4]))

        print()

    

    # method to take id input of doctor from which patient want to take appointment
    def id_for_appointment(self):
        while True:
            # calling methods to get all doctor names and check any doctor avaliable at medicare or not
            data=self.get_doc_names()
            check_data=self.fetch_data_from_accounts()
            if not data:
                return
        
            # id input of doctor he want to set appointment
            try:
                self.display_doctors_to_patients()
                
                # Taking doctor id input
                doc_id=int(input("\nEnter Doctor Id You Want to get appointment (enter 0 to back):"))
                
                # space for back
                if doc_id==0:
                    return
                
                # Checking that doctor id exists in account table or not
                for doctor in check_data:
                    if doctor[0]==doc_id:
                        print(f"\nDoctor-Id Found You Want to get Appointment From {doctor[1]}\n")
                        return (doc_id,doctor[1],doctor[3])
                    
                print("\nDoctor-Id Not Found Please Enter Correct Id.\n")
            
            except ValueError:
                print('Please Enter In Digits\n')
    

    
    # Method to generate random 4 digit checkup id for patients also save id to file to ensure that id not repaetaed
    def generate_checkup_id(self):
       
        # check if file already exists
        if os.path.exists("checkup_id.txt"):
            with open("checkup_id.txt","r") as file:
                id_list=file.readlines()
                id_list=[int(id.strip()) for id in id_list]
        else:
            id_list=[]

        # generate random id
        while True:
            id=random.randint(1000,9999)
            if id not in id_list:
                id_list.append(id)
                with open("checkup_id.txt","a") as file:
                    file.write(str(id)+"\n")
                return id

    # method to Take disease name input only alphabets and spaces allowed
    def get_disease(self):
        while True:
            # Taking input of disesase name
            disease=input("Enter Your Disease Name (enter 0 to back):").strip()
            
            # If He want to go back
            if disease=="0":
                return
            

            # If getting null input
            if disease=="":
                print("\nDisease Name Can't be Empty.Please Enter Correct Disease Name\n")
            
            # if getting any other thing from alphabets and spaces
            elif not disease.replace(" ","").isalpha():
                print("\nDisease Name Can only contain alphabets and spaces.Please Enter Correct Disease Name\n")
            
            # When all conditions are met
            else:
                return disease
    
    # method to set appointment status by default it is pending
    def appointment_status(self):
        return "Pending"
    

    #method to first show him numbers of month like 1 january 2 feburary and so on then take input from user
    def appointment_month(self):

        # make dictionary key number and value month then take input from user
        month_dict={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

       # now take input from user
        while True:
            print("\n\tMonths Avaliable For Appointment.\n")
            for key,value in month_dict.items():
                print(f"{key}-{value}")

            # Taking month input
            month=int(input("\nEnter Month For Appointment (enter 0 to back):"))
            
            # If He want to go back
            if month==0:
                return
            
            # If month is not in range 1 to 12
            if month<1 or month>12:
                print("\nMonth Must be between 1 to 12.Please Enter Correct Month\n")
            
            # If month is in range 1 to 12
            else:
                return month_dict[month] 
       
    
    # method to set medicines you got by default it is empty
    def medicines_you_got(self):
        return "Not-Provided"



    # method to set appointment date take input from user also check date must be between 1 to 31
    def appointment_date(self):
        while True:
            try:       # Use try except to avoid conflicts

                # Taking date input
                date=int(input("Enter Date For Appointment (enter 0 to back):"))

                # If he want to go back
                if date==0:
                    return
                
                # If date is not between 1 to 31
                if date<1 or date>31:
                    print("\nDate Must be between 1 to 31.Please Enter Correct Date\n")

                # If date is between 1 to 31
                else:
                    return date
                
            # If getting date in other than digits
            except ValueError:
                print("Please Enter In Digits\n")




    # method for patients to set appointments
    def set_appoitments(self):
        # calling respetive methods to take input
        
        result = self.id_for_appointment()
        if result is None:
            return  # Exit if the user wants to go back

        # unpacking tuple
        id, doc_name, doc_user_id = result
        
        # chenge self.doc_table to doc_user_id
        self.doc_table=doc_user_id
        
        # calling generate checkup id method
        doc_id=self.generate_checkup_id()
        # Checking if get input
        if doc_id:
            disease=self.get_disease()

            # Checking if disease:
            if disease:
                appointment_month=self.appointment_month()
                

                # Checking if appointment date
                if appointment_month:
                    appointment_date=self.appointment_date()
                    # concatenate date and month
                    appointment_date=f"{appointment_date}-{appointment_month}"

                    # Checking if get month
                    if appointment_date:
                        appointment_status=self.appointment_status()
                        checkup_id=self.generate_checkup_id()
                        medicines_you_got=self.medicines_you_got()

                        # After getting all inputs
                        # insert data in doctors table
                        self.insert_data_in_doctors_appointments_table(checkup_id,self.table_accounts,disease,appointment_date,appointment_status,medicines_you_got,self.table_accounts)


                        # insert data in patients table
                        self.insert_data_in_appointments_patients_table(checkup_id,doc_name,disease,appointment_date,appointment_status,medicines_you_got)

                        print("\nAppointment Set Successfully.\n")
                        print(f"Your Checkup Id is {checkup_id}\n")
                        print(f"Your Appointment Date is {appointment_date}-{appointment_month}\n")
                        print(f"Your Appointment Status is {appointment_status}\n")
                        print(f"Your Doctor Name is {doc_name}\n")
                        print(f"Your Disease is {disease}\n")
                        print(f"Your Medicines You Got is {medicines_you_got}\n")
                        print()
                        return
                    
                    # When not geeting month
                    else:
                        print("\nAppointment Month Not Entered Correctly.Please Enter Correct Appointment Month\n")

                # When not getting date
                else:                  
                    print("\nAppointment Date Not Entered Correctly.Please Enter Correct Appointment Date\n")

            # When not getting disease
            else:
                print("\nDisease Not Entered Correctly.Please Enter Correct Disease\n")
        # When not getting doctor id
        else:
            print("\nDoctor Id Not Entered Correctly.Please Enter Correct Doctor Id\n")



            
        
    # method to display all appointments of patients
    def display_appointments_patients(self):
        # query to fetch data from patients table
        fetch_query=f"SELECT * FROM hospital.{self.table_accounts}"
        self.cursor.execute(fetch_query)
        data=self.cursor.fetchall()

       # Check if data is there
        if data:
            print("\t\tYour Appointments Details\n\n")
            print("{:<15} {:<20} {:<15} {:<20} {:<20} {:<20}".format(
                "Checkup-Id", "Doctor-Name", "Disease", "Appointment-Date", "Appointment-Status", "Medicines-Got"))
            print("-" * 110)
            for item in data:
                print("{:<15} {:<20} {:<15} {:<20} {:<20} {:<20}".format(
                    item[0], item[1], item[2], item[3], item[4], item[5]))
            print()
        else:
            print("\nNo Appointments Yet.\n")


        


class Doctors(Patients):
    def __init__(self, doctor_table, patient_table):  # Add patient_table as a parameter
        self.table_doctor = doctor_table
        self.patient = ""
        self.pat_list = []
        super().__init__(patient_table)  # Pass patient_table to the Patients class constructor
    
    # main page for doctors
    def main_page_doctors(self):
        print("\tWelcome In Medi-Care\n\n")
        # loop to stuck him till he want to go back
        while True:
            # Display options for doctors
            print("\t1.See Your Profile.")
            print("\t2.Update Your Profile.")
            print("\t3.See Your Appointments.")
            print("\t4.Give Medicines to Patients.")
            print("\t5.Change Appointment Status of Patients.")
            print("\t6.Back From MediCare Doctors Hub.\n\n")
            

            # taking doctors chouce
            doc_choice=input("Dear Doctor Enter Your Choice:").strip()

            # handling choice and calling respective methods
            if doc_choice=="1":
                self.view_profile_doctors()   # call profile method

            elif doc_choice=="2":
                self.update_profile_doctors()  # call method to update profile

            elif doc_choice=="3":
                self.display_appointments_doctors()   # call method to display appointments

            elif doc_choice=="4":
                self.suggest_medicines()   # call method to suggest medicines

            
            elif doc_choice=="5":
                self.change_appointment_status()     # calling method for changing appointmenr

            # exit option for doctor
            elif doc_choice=="6":
                print("\nBack From MediCare Doctors Hub..\n")
                return
            
            # Invalid choice
            else:
                print("Invalid Choice.Please Enter Correct Choice\n\n")

     
    # method to print doctor profile details from accounts table checking user id
    def view_profile_doctors(self):
        # calling fetch data method to get data
        data=self.fetch_data_from_accounts()
        
        print("\t\tProfile's Details\n")
        print("{:<10} {:<20} {:<30} {:<15} {:<15}".format("Id", "Doctor-Name", "Gmail", "User-Id", "Password"))
        print("-" * 100)
        # Iterate over data
        for item in data:
            # Check if user id is equal to doctor's table
            if item[3] == self.table_doctor:
                print("{:<10} {:<20} {:<30} {:<15} {:<15}".format(item[0], item[1], item[2], item[3], item[4]))

        print()

    # method to give options to doctors to update profile
    def update_profile_doctors(self):
        print("\t\tUpdate Your Profile\n\n")
        while True:
             # call view profile method to show profile
            self.view_profile_doctors()

            # Display options for doctors
            print("\t1.Update Your Name.")
            print("\t2.Update Your Gmail.")
            print("\t3.Update Your Password.")
            print("\t4.Back From Update Profile.\n")
            
           

            # taking doctors choice
            doc_choice=input("Dear Doctor Enter Your Choice For Updation:").strip()

            # handling choice and calling respective methods
            if doc_choice=="1":
                # check if name is updated

                name=self.get_name()  # call method to update name
                if name:
                    # update in accounts table where user id is equal to doctor table
                    update_query=f"UPDATE hospital.accounts_hosp SET name='{name}' WHERE user_id='{self.table_doctor}'"
                    self.cursor.execute(update_query)
                    self.conn.commit()
                    print("\nName Updated Successfully.\n")


            elif doc_choice=="2":
                gmail=self.get_gmail()
                if gmail:
                    # update in accounts table where user id is equal to doctor table
                    update_query=f"UPDATE hospital.accounts_hosp SET gmail='{gmail}' WHERE user_id='{self.table_doctor}'"
                    self.cursor.execute(update_query)
                    self.conn.commit()
                    print("\nGmail Updated Successfully.\n")
            

            elif doc_choice=="3":
                password=self.get_password()
                if password:
                    # update in accounts table where user id is equal to doctor table
                    update_query=f"UPDATE hospital.accounts_hosp SET password='{password}' WHERE user_id='{self.table_doctor}'"
                    self.cursor.execute(update_query)
                    self.conn.commit()
                    print("\nPassword Updated Successfully.\n")

            elif doc_choice=="4":
                print("Back From Update Profile..")
                return
            
            else:
                print("\nInvalid Choice.Please Enter Correct Choice\n\n")


    # method to print details that is self.doctor_table except last index because of patietnts user id
    # also check if table empty so say that no patient made appointment yet
    def display_appointments_doctors(self):
        # query to fetch data from doctors table
        fetch_query=f"SELECT * FROM hospital.{self.table_doctor}"
        self.cursor.execute(fetch_query)
        data=self.cursor.fetchall()

        # Check if data is there
        if data:
            print("\t\tYour Appointments Details\n\n")
            print("{:<15} {:<20} {:<15} {:<20} {:<20} {:<20}".format(
                "Checkup-Id", "Patient-Name", "Disease", "Appointment-Date", "Appointment-Status", "Medicines-Suggested"))
            print("-" * 110)
            for item in data:
                print("{:<15} {:<20} {:<15} {:<20} {:<20} {:<20}".format(
                    item[0], item[1], item[2], item[3], item[4], item[5]))
            print()
            return "something"

        else:
            print(f"\nSorry Doctor No Appointments Yet.\n")
 
    

    # method to fetch data from table doctors
    def fetch_data_from_doctors(self):
        # query to fetch data from doctors table
        fetch_query=f"SELECT * FROM hospital.{self.table_doctor}"
        self.cursor.execute(fetch_query)
        data=self.cursor.fetchall()
        return data


    # method to suggest medicine to patients by doctor check if any appointment mean data in table then take id input vfrom doctor to whom he want to suggest medicine then change in doctor table also that row in doctor table take last element that is patient user id open that table also make change here
    def suggest_medicines(self):
        # callimg display appointments method to show appointments
        result=self.display_appointments_doctors()
        if result is None:
            return
        # calling fetch data method to get data
        data=self.fetch_data_from_doctors()

        
        
        

        # taking input of checkup id
        while True:
            # call display appointments method to show appointments
            result=self.display_appointments_doctors()
            try:
                checkup_id=int(input("Enter Checkup Id You Want to Suggest Medicines (enter 0 to back):"))
                if checkup_id==0:
                    return
                
                # check that checkp id is in data
                
                for item in data:
                    if item[0]==checkup_id:
                        # taking medicines input
                        medicines=input("Enter Medicines You Want to Suggest (enter 0 to back):").strip()
                        if medicines=="0":
                            return
                        
                        # condition it must not empty
                        if medicines=="":
                            print("\nMedicines Can't be Empty.Please Enter Correct Medicines\n")
                            continue
                         
                        self.cursor.execute("USE hospital")
                        # update in doctors table where checkup id is equal to checkup id
                        update_query=f"UPDATE {self.table_doctor} SET medicines_you_suggested='{medicines}' WHERE id={checkup_id}"
                        self.cursor.execute(update_query)
                        self.conn.commit()
                        print("\nMedicines Suggested Successfully.\n")


                       # getting last element from that row
                        patient_user_id=item[-1]
                        # update patient user id table where id = checkup id change medicine you got to medicines give by doctor
                        self.cursor.execute(f"UPDATE {patient_user_id} SET medicines_you_got='{medicines}' WHERE id={checkup_id}")
                        self.conn.commit()
                        return
                    
                # if checkup id not found
                print("\nCheckup Id Not Found.Please Enter Correct Checkup Id\n")

            # if getting checkup id in other than digits
            except ValueError:
                print("Please Enter In Digits\n")

    # method to change appointment status of patients by doctor check if any appointment mean data in table then take id input vfrom doctor to whom he want to suggest medicine then change in doctor table also that row in doctor table take last element that is patient user id open that table also make change here
    def change_appointment_status(self):
        # callimg display appointments method to show appointments
        result=self.display_appointments_doctors()
        if result is None:
            return
        
        data=self.fetch_data_from_doctors()   # fetch data from doctors table

        # taking input of checkup id
        while True:
            # call display appointments method to show appointments
            result=self.display_appointments_doctors()
            try:
                checkup_id=int(input("Enter Checkup Id You Want to Change Appointment Status (enter 0 to back):"))
                if checkup_id==0:
                    return
                # check if checkup id is in data
                for item in data:
                    if item[0]==checkup_id:

                        # taking appointment status input
                        appointment_status=input("Enter Appointment Status You Want to Change (enter 0 to back):").strip().lower()
                        if appointment_status=="0":
                            return
                        
                        # condition it must not empty
                        if appointment_status=="":
                            print("\nAppointment Status Can't be Empty.Please Enter Correct Appointment Status\n")
                            continue

                        # only input allowed approved or cancelled
                        if appointment_status!="approved" and appointment_status!="cancelled":
                            print("\nAppointment Status Can only be Approved or Cancelled.Please Enter Correct Appointment Status\n")
                            continue

                        self.cursor.execute("USE hospital")
                
                        # update in doctors table where checkup id is equal to checkup id
                        update_query=f"UPDATE hospital.{self.table_doctor} SET appointment_status='{appointment_status}' WHERE id={checkup_id}"
                        self.cursor.execute(update_query)
                        self.conn.commit()
                        print("\nAppointment Status Changed Successfully.\n")


                        # now open that table of patient and update that row also
                        patient_user_id=item[-1]
                        # update patient user id table where id = checkup id change appointment status to appointment status given by doctor
                        self.cursor.execute(f"UPDATE {patient_user_id} SET appointment_status='{appointment_status}' WHERE id={checkup_id}")
                        self.conn.commit()
                        
                       



                        return
                    
                # if checkup id not found
                print("\nCheckup Id Not Found.Please Enter Correct Checkup Id\n")

            # if getting checkup id in other than digits
            except ValueError:
                print("Please Enter In Digits\n")







c=Connection()
database=Database_for_Hospital()
database.create_database()
database.create_table_for_accounts_hospital()
s=Signup()
l=Login()

                   


# main function for program execution

def main():
    print("\t\tWelcome To Medi-Care\n\n")
    while True:
        # apply loop[ to stuck till he want to out
        print("\t1.Proceed For Registration")
        print("\t2.Proceed For Login")
        print("\t3.Exit From Medi-Care\n")

        # taking users choice
        choice=input("Enter your choice to proceed Further:").strip()

        # handle the choice
        if choice=="1":
            s.type_account()

        elif choice=="2":
            l.login_process()
            




        
        elif choice=="3":
            # exiting the system
            print("Hope you Satisfied with our services\nMedicare is now exiting..see you later!")
            break

        else:
            print("Invalid Choice.Dear Please Ebnter From Given Choices\n\n")

main()