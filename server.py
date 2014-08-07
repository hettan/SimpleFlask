from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def root():
    return "Hej "

@app.route("/hej/<name>")
def say_hej(name):
    return "hej "+name

@app.route("/say_hej")
def say_hej2():
    name = request.args.get("name")
    year = request.args.get("year")
    return say_hej(name) + "year " + year

if __name__ == "__main__":
    app.run(debug=True)
