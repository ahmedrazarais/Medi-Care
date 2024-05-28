from Patients_Area import Patients




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