import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.hospital_service_impl import HospitalServiceImpl
from entity.models import Appointment
from exception.allexception import PatientNumberNotFoundException

def display_menu():
    print("\n=== Hospital Management System ===")
    print("1. Get Appointment by ID")
    print("2. Get Appointments for a Patient")
    print("3. Get Appointments for a Doctor")
    print("4. Schedule a New Appointment")
    print("5. Update Appointment")
    print("6. Cancel Appointment")
    print("0. Exit")

def main():
    service = HospitalServiceImpl()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                aid = int(input("Enter appointment ID: "))
                app = service.get_appointment_by_id(aid)
                print(app if app else "No appointment found.")
            elif choice == "2":
                pid = int(input("Enter patient ID: "))
                apps = service.get_appointments_for_patient(pid)
                for app in apps:
                    print(app)
            elif choice == "3":
                did = int(input("Enter doctor ID: "))
                apps = service.get_appointments_for_doctor(did)
                for app in apps:
                    print(app)
            elif choice == "4":
                pid = int(input("Patient ID: "))
                did = int(input("Doctor ID: "))
                date = input("Date (YYYY-MM-DD): ")
                desc = input("Description: ")
                app = Appointment(None, pid, did, date, desc)
                if service.schedule_appointment(app):
                    print("Appointment scheduled successfully.")
            elif choice == "5":
                aid = int(input("Appointment ID to update: "))
                pid = int(input("New Patient ID: "))
                did = int(input("New Doctor ID: "))
                date = input("New Date (YYYY-MM-DD): ")
                desc = input("New Description: ")
                app = Appointment(aid, pid, did, date, desc)
                if service.update_appointment(app):
                    print("Appointment updated successfully.")
            elif choice == "6":
                aid = int(input("Appointment ID to cancel: "))
                if service.cancel_appointment(aid):
                    print("Appointment canceled.")
                else:
                    print("Cancellation failed.")
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except PatientNumberNotFoundException as e:
            print("Error:", e)
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
