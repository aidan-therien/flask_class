#server.py

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def server_on():
    return "The server is on"


@app.route("/info", methods = ["GET"])
def info():
    info_string = "The server calculates the ideal weith"
    "of a person based on their height, age, and gender"
    calc_info_string = "The calculation can accept a POST"
    "with the following format"
    return jsonify({"calc_info_string": calc_info_string,
                   "Info_string": info_string})


@app.route("/iwc", methods=["POST"])
def ideal_weight():
    in_data = request.get_json()
    age = in_data["age"]
    gender =in_data["gender"]
    height = in_data["height_in"]
    ideal_weight_kg = 48.0 + 2.7 * (height - 60)
    ideal_weight_lb = ideal_weight_kg * 2.20462
    answer = {"Input_data": in_data, "ideal_weight": ideal_weight_lb}

@app.route("hello/<yourname>", methods = ["GET"])
def sayhello(yourname):
    return "Hello, {}".format(yourname)

if __name__ == "__main__":
    app.run()
