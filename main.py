import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

df = pd.read_csv('EU_temperature_data/stations.txt', skiprows=17, nrows=92)
station_list = df[['STAID', 'STANAME                                 ']]


@app.route("/")
def home():
    return render_template("home.html", data=station_list.to_html())


@app.route("/api/in/<year>/<month>")
def indtempdata(year, month):
    month = month.upper()
    ind_df = pd.read_csv('IN_temperatures/temperatures.csv')
    temperature = ind_df.loc[ind_df['YEAR'] == int(year)][month].squeeze()
    if isinstance(temperature, pd.Series):
        return {
            "message": "Data not found for given query. Please try again for different values."
        }
    else:
        return {
            "Month and Year": month + "-" + str(year),
            "Temperature": temperature
        }


@app.route("/api/eu/<station>/<date>")
def eutempdata(station, date):
    filename = "EU_temperature_data/" + "TG_STAID" + str(station).zfill(6) + ".txt"
    eu_df = pd.read_csv(filename, skiprows=20)
    temperature = eu_df.loc[eu_df['    DATE'] == int(date)]['   TG'].squeeze() / 10
    if isinstance(temperature, pd.Series):
        return {
            "message": "Data not found for given query. Please try again for different values."
        }
    else:
        result = {
            "Temperature": temperature,
            "Date": str(date)[:4] + '-' + str(date)[4:6] + '-' + str(date)[6:8],
            "Station": station
        }
        return result


if __name__ == "__main__":
    app.run(debug=True)
