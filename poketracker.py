from flask import Flask, render_template, request, jsonify
import json
import pandas as pd
import plotly.express as px

app = Flask(__name__)


@app.route('/')
def index():
    title = 'PokeTracker App'
    subtitle = 'testing'
    content = 'Gotta Track ''em All!'
    params = {
        'title': title,
        'subtitle': subtitle,
        'content': content
    }
    return render_template('simpleindex.html', params=params)


if __name__ == '__main__':
    app.run()