from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

station = pd.read_csv("Files/stations.txt", skiprows=17)
station=station[["STAID","STANAME                                 "]]
@app.route("/")
def home():

    return render_template("home.html", data = station.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "Files/TG_STAID"+str(station).zfill(6)+".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    date = date[:4] + "-" + date[4:6] + "-" + date[6:8]
    temp = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    dict = {"Station": station, "date": date, "temperature": temp}
    return dict

app.run(debug=True)