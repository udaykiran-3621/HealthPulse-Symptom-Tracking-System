from patient import *
from symptom import *
from reports import *

def menu():
    while True:
        print("\n===== HealthPulse =====")
        print("1. Add Patient")
        print("2. Add Symptom")
        print("3. View Patients")
        print("4. View Symptoms")
        print("5. Report")
        print("6. Exit")

        ch = input("Enter choice: ")

        if ch=="1":
            add_patient()

        elif ch=="2":
            add_symptom()

        elif ch=="3":
            view_patients()

        elif ch=="4":
            view_symptoms()

        elif ch=="5":
            generate_report()

        elif ch=="6":
            break

        else:
            print("Invalid Choice")