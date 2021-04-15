from flask import render_template, request
from app import app
from modules.event_list import events
from modules.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title = "Home", events = events)