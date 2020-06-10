#server.py

from flask import Flask, jsonify, request
from datetime import datetime
app = Flask(__name__)

@app.route("/time", methods = ["GET"])
def server_on():
    datetime_variable = datetime.now()
    date = datetime.strftime(datetime_variable, "%m-%d-%y %H:%M:%S")
    time = date.split(" ")[1]
    return time


@app.route("/date", methods = ["GET"])
def server_on1():
    curr_date = datetime.now()
    time = datetime.strftime(curr_date, "%m-%d-%y %H:%M:%S")
    date = time.split(" ")[0]
    return date


@app.route("/age", methods = ["POST"])
def server_on2():
    in_data = request.get_json()
    data_time = in_data["date"]
    time_obj = datetime.strptime(data_time,"%m/%d/%Y")
    curr_date = datetime.date()
    delta = curr_date-time_obj
    return delta.days

if __name__ == "__main__":
    app.run()
