from flask import Flask, render_template, request, jsonify
import json
import pandas as pd
import plotly.express as px

app = Flask(__name__)


def get_graph(period='JJA'):
    df = pd.read_csv('static/GlobalTemps1880-2022.csv')
    fig = px.bar(df, x='Year', y=period,
                 color=period, title=period,
                 color_continuous_scale='reds',
                 template='plotly_white', width=1000, height=500)
    graph_json = fig.to_json()
    return json.dumps(graph_json)

#### App ####

@app.route('/')
def index():
    params = {
        'title': 'PokeTracker'
    }
    return render_template('index.html', params=params)

@app.route('/simple')
def simpleindex():
    header = 'Global Temperature'
    subheader = 'Global Temperature changes over last few centuries'
    description = '''
    The graph shows increase in temperature year over year.
    The data spans from 1881 to 2022 and includes anomalies for the months of June through August.
    '''
    menu_label = 'Select a period'
    options = [
        {'code': 'J-D', 'desc': 'Whole year'},
        {'code': 'DJF', 'desc': 'Winter (North)'},
        {'code': 'MAM', 'desc': 'Spring (North)'},
        {'code': 'JJA', 'desc': 'Summer (North)'},
        {'code': 'SON', 'desc': 'Autumn/Fall (North)'}
    ]
    params = {
        'template': 'simpleindex.html',
        'title': header,
        'subtitle': subheader,
        'content': description,
        'menu_label': menu_label,
        'options': options,
        'graph': get_graph()
    }


    return render_template(params.get('template'), params=params)

@app.route('/callback', methods=['POST'])
def callback():
    if request.is_json:
        data = request.get_json()
        return get_graph(period=data['dropdown'])
    else:
        return jsonify({'error': 'Invalid JSON data'}), 400


if __name__ == '__main__':
    app.run()