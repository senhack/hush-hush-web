from flask import render_template, request
from app import app
import json, requests

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
    return render_template('floors.html',
                            title='Floors')

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
