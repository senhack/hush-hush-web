from flask import render_template, request
from app import app
from datetime import datetime, timedelta

import json, requests, os

# import functions

## specify main menu
header_menu = [
    {
        'title' : 'Home',
        'uri'   : '/'
    },
    {
        'title' : 'Floors',
        'uri'   : '/floors'
    },
    {
        'title' : 'About',
        'uri'   : '/about'
    }
]

## app context processor
@app.context_processor
def inject_user():
    return dict(header_menu=header_menu)

## app routes
@app.route('/')
def home():
    return render_template('home.html',
                            title='Home')

@app.route('/floors')
def music():
    headers = { 'Content-type': 'application/json', 'x-api-key': os.environ['SHUSH_API_KEY'] }
    current_time = datetime.now()
    start_date = current_time - timedelta(minutes=1)
    end_date = current_time

    response = requests.get(("https://%s/test/StoreAudioData?device_id=device-0002&start_date=%s&end_date=%s" % (os.environ['SHUSH_API_ENDPOINT'], start_date.strftime("%Y%m%d%H%M%S"), end_date.strftime("%Y%m%d%H%M%S"))), headers=headers)
    response_data = response.json()
    record = response_data['Items'][-1]

    color = '#BBBBBB'
    max_amplitude = float(record['MaximumAmplitude'])
    if max_amplitude > 0.5:
        color = '#FFB33a'
    else if max_amplitude > 0.9:
        color = '#D10808'

    return render_template('floors.html',
                            title='Floors', color=color)

@app.route('/about')
def about():
    return render_template('about.html',
                            title='About')

## custom error pages
@app.errorhandler(403)
def page_not_found(e):
    return render_template('error.html', message='Forbidden', code='403'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message='Page not found', code='404'), 404

@app.errorhandler(405)
def page_not_found(e):
    return render_template('error.html', message='Method not allowed', code='405'), 405
