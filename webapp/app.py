from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Head to /getJokes for Chuck Norris Jokes!'


@app.route('/getJokes')
def getJokes():
    jokes = ''
    for i in range(10):
        response = requests.get("http://api.icndb.com/jokes/random/")
        response_json = response.json()
        joke = response_json["value"]['joke']
        jokes += joke + '\n'

    return render_template('index.html', jokes=jokes)


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')