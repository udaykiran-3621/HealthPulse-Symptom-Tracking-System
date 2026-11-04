import json
import os

def load(filename):
    if not os.path.exists(filename):
        return []

    with open(filename,"r") as f:
        return json.load(f)

def save(filename,data):
    with open(filename,"w") as f:
        json.dump(data,f,indent=4)