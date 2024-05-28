from Registration_Functionality import Signup





# class for login and inherits with signup class for multilevel inheritance
class Login(Signup):
    def __init__(self):
        self.login_type = ""  # Initialize login type
        self.doc_table = ""
        self.patient_table = ""
        super().__init__()  # Call parent constructor

    # Method for the login process
    def login_process(self):
        # from hospital_system import Doctors, Patients
        from Doctors_Area import Doctors
        from Patients_Area import Patients
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

  
      


