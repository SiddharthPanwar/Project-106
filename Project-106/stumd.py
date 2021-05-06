import plotly.express as px
import csv 
with open("STUMD.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Present",y="Marks")
    fig.show()