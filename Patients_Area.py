# importing mysql and from config file details for connection
import mysql.connector
import os
import random

from Login_Procedure import Login









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
            print("No Doctors Avaliable At This Moment.\n")
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
