# Medi-Care System

## Overview

The Medi-Care System is a console-based application designed to manage patient and doctor interactions in a hospital environment. It allows patients to update their profiles, set appointments, and view their appointments. Doctors can view and update their profiles, see their appointments, suggest medicines to patients, and change appointment statuses.

## Features

### For Patients
- **Update Profile:** Patients can update their name, email, and password.
- **View Profile:** Patients can view their profile details.
- **Set Appointments:** Patients can set appointments with doctors by selecting a doctor, specifying their disease, and choosing an appointment date.
- **View Appointments:** Patients can view their appointment details.Patients can be free to make appointment by any doctor in Medi-Care.

### For Doctors
- **Update Profile:** Doctors can update their name, email, and password.
- **View Profile:** Doctors can view their profile details.
- **View Appointments:** Doctors can view their appointments with patients.
- **Suggest Medicines:** Doctors can suggest medicines to patients based on their appointments.
- **Change Appointment Status:** Doctors can change the status of appointments (e.g., approved, cancelled).

## Project Structure

The project contains several classes, each responsible for different parts of the system:

- `Connection`: Handles database connection.
- `Database_for_Hospital`: Manages database creation and table setup.
- `Signup`: Handles the registration process for new users.
- `Login`: Manages the login process for existing users.
- `Patients`: Contains methods for patient-related functionalities.
- `Doctors`: Extends the `Patients` class and includes additional methods for doctor-related functionalities.

## Classes and Methods

### Connection
Handles the connection to the database.

### Database_for_Hospital
- **create_database()**: Creates the database if it doesn't exist.
- **create_table_for_accounts_hospital()**: Creates the accounts table in the database.

### Signup
- **type_account()**: Prompts user to choose account type (patient or doctor) and proceed with registration.

### Login
- **login_process()**: Manages the login process, verifying user credentials and directing to the appropriate menu (patient or doctor).

### Patients
- **update_profile_patients()**: Allows patients to update their profile information.
- **view_profile_patients()**: Displays the patient's profile.
- **id_for_appointment()**: Prompts the patient to select a doctor for an appointment.
- **generate_checkup_id()**: Generates a unique checkup ID for the appointment.
- **get_disease()**: Prompts the patient to enter their disease.
- **appointment_status()**: Returns the default appointment status ("Pending").
- **appointment_month()**: Prompts the patient to choose a month for the appointment.
- **medicines_you_got()**: Returns the default medicine status ("Not-Provided").
- **appointment_date()**: Prompts the patient to choose a date for the appointment.
- **set_appoitments()**: Manages the entire process of setting an appointment for a patient.
- **display_appointments_patients()**: Displays all appointments for the logged-in patient.

### Doctors
Extends the `Patients` class and includes additional functionalities for doctors.
- **main_page_doctors()**: Displays the main menu for doctors.
- **view_profile_doctors()**: Displays the doctor's profile.
- **update_profile_doctors()**: Allows doctors to update their profile information.
- **display_appointments_doctors()**: Displays all appointments for the logged-in doctor.
- **fetch_data_from_doctors()**: Fetches data from the doctors table.
- **suggest_medicines()**: Allows doctors to suggest medicines to patients.
- **change_appointment_status()**: Allows doctors to change the status of appointments.

## How to Run the Project

1. **Ensure you have the required dependencies installed.**
   - Python 3.x
   - MySQL connector for Python (`mysql-connector-python`)
   - `os`, `random` modules (standard Python libraries)

2. **Setup the Database**
   - Ensure MySQL server is running.
   - Create a database named `hospital` or adjust the code to use a different database name.

3. **Setup the Config.py File**
   - Make Sure You Must Update config.py File Before Running main_program.py File Change variables with your database details. 
  


## Technology Used
- Programming Language: Python
- Database: MySQL
### Author
- Project made by Ahmed Raza
- Email: razarais28@gmail.com