from flask import Flask
from flask import request

app = Flask(__name__)
@app.route("/") 
def root():
    return "hej"

@app.route("/<name>/hej") 
def hej(name):
    return "nooo " + name

@app.route("/say_hej") 
def say_hej():
    name = request.args.get("name")
    return hej(name)


if __name__ == "__main__":
    app.run()
