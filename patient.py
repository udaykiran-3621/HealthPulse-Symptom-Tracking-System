from storage import *

FILE="data/patients.json"

def add_patient():
    patients=load(FILE)

    pid=input("Patient ID: ")
    name=input("Name: ")
    age=input("Age: ")

    patients.append({
        "id":pid,
        "name":name,
        "age":age
    })

    save(FILE,patients)

    print("Patient Added")

def view_patients():
    patients=load(FILE)

    for p in patients:
        print(p)