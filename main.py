import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

df = pd.read_csv('EU_temperature_data/stations.txt', skiprows=17, nrows=92)
station_list = df[['STAID', 'STANAME                                 ']]


@app.route("/")
def home():
    return render_template("home.html", data=station_list.to_html())


@app.route("/api/ind/<year>/<month>")
def indtempdata(year, month):
    month = month.upper()
    df = pd.read_csv('IN_temperatures/temperatures.csv')
    temperature = df.loc[df['YEAR'] == int(year)][month].squeeze()

    return {
        "Month and Year": month + "-" + str(year),
        "Temperature": temperature
    }


@app.route("/api/eu/<station>/<date>")
def eutempdata(station, date):
    filename = "EU_temperature_data/" + "TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    temperature = df.loc[df['    DATE'] == int(date)]['   TG'].squeeze() / 10
    return {
        "Temperature": temperature,
        "Date": str(date)[:4] + '-' + str(date)[4:6] + '-' + str(date)[6:8],
        "Station": station
    }


if __name__ == "__main__":
    app.run(debug=True)
