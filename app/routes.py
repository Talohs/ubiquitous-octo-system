from app import batter
from flask import render_template

@batter.route("/")
def index():
    return render_template('index.html')

@batter.route("/fave_five")
def fav_bands():
    # bands = {
    #     'Band1':['The Offspring','Americana'],
    #     'Band2':['System of a down', 'Steal this Album'],
    #     'Band3':['Muse','The 2nd Law'],
    #     'Band4':['Led Zeppelin', 'Led Zeppelin II'],
    #     'Band5':['The Beatles', 'Revolver']
    # }
    
    bands = ['The Offspring', 'System of a down', 'Muse', 'Led Zeppelin', 'The Beatles']

    return render_template('fave_five.html', bands=bands)