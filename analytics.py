from storage import *

def total_cases():

    symptoms=load("data/symptoms.json")

    return len(symptoms)