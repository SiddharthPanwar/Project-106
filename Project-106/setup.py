import plotly.express as px
import csv 
import numpy as np 

def getDataSrc(data_path):
    marks = []
    present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks"]))
            present.append(float(row["Present"]))
    return {"x":marks,"y":present}

def findcorrelation(data_src):
    correlation = np.corrcoef(data_src["x"],data_src["y"])
    print("correlation between marks vs attendance : ",correlation[0,1])

def setup():
    data_path = "STUMD.csv"
    data_src = getDataSrc(data_path)
    findcorrelation(data_src)

setup()
    
    