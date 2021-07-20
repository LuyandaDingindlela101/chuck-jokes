from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    joke_details = requests.get(api_url).json()

    return render_template("view_joke.html", joke_details=joke_details)