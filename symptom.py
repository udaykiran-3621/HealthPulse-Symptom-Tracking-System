from storage import *

FILE="data/symptoms.json"

def add_symptom():

    symptoms=load(FILE)

    pid=input("Patient ID: ")
    symptom=input("Symptom: ")
    severity=input("Severity: ")
    date=input("Date: ")

    symptoms.append({
        "patient":pid,
        "symptom":symptom,
        "severity":severity,
        "date":date
    })

    save(FILE,symptoms)

    print("Saved")

def view_symptoms():

    symptoms=load(FILE)

    for s in symptoms:
        print(s)