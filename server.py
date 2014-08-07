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
    hep = request.args.get("hep");
    return hej(name) + " " + hep

@app.route("/hej_count")
def hej_count():
    times = request.args.get("times")
    return "HEEE "*int(times)
    
if __name__ == "__main__":
    app.run()
