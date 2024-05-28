from Database_Connection import Connection
from Database_Creation import Database_for_Hospital
from Registration_Functionality import Signup
from Login_Procedure import Login




# creating object of classes
c=Connection()
database=Database_for_Hospital()
database.create_database()
database.create_table_for_accounts_hospital()
s=Signup()
l=Login()


                   


# main function for program execution

def main():
    print("\n\t\tWELCOME TO  MEDI-CARE\n")
    print("If you are new to Medi-Care then please register yourself first to proceed further\nOtherwise Just login with your credentials\n")
    while True:
        # apply loop[ to stuck till he want to out
        print("\t1.Proceed For Registration In Medi-Care.")
        print("\t2.Proceed For Login In Medi-Care.")
        print("\t3.Exit From Medi-Care\n")

        # taking users choice
        choice=input("Enter your choice to proceed Further:").strip()

        # handle the choice
        if choice=="1":
            s.type_account()

        # login process
        elif choice=="2":
            l.login_process()
            

        # Exiting the system
        elif choice=="3":
            # exiting the system
            print("\nHope you Satisfied with our services\nMedicare is now exiting..\nsee you later!\n")
            break

        else:
            print("Invalid Choice.Dear Please Ebnter From Given Choices\n\n")

main()    # calling main function to start the program