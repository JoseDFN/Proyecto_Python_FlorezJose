import os
import json

MY_DATABASE = None  # Define the path to your database file

def NewFile(*param):
    with open(MY_DATABASE, "w") as wf:
        json.dump(param[0], wf, indent=4)

def ReadFile():
    with open(MY_DATABASE, "r") as rf:
        return json.load(rf)

def checkFile(*param):
    data = list(param)
    if os.path.isfile(MY_DATABASE):
        if len(param):
            data[0].update(ReadFile())
    else:
        if len(param):
            NewFile(data[0])