import requests
from flask import Flask
app=Flask(__name__)
@app.route("/")
def all_elephant():
    response=requests.get("https://elephant-api.herokuapp.com/elephants")
    data=response.json()
    return data
@app.route("/random")
def random_elephant():
    response=requests.get("https://elephant-api.herokuapp.com/elephants/random")
    data=response.json()
    return data
@app.route("/sex/<sex>")
def by_Sex(sex):
    response=requests.get(f"https://elephant-api.herokuapp.com/elephants/sex/{sex}")
    data=response.json()
    return data
@app.route("/name/<name>")
def by_name(name):
    response=requests.get(f"https://elephant-api.herokuapp.com/elephants/name/{name}")
    data=response.json()
    return data
app.run(debug=True)