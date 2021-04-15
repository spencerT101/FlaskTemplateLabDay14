from flask import render_template, request
from app import app
from modules.event_list import events, add_new_event
from modules.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title = "Home", events = events)

@app.route('/events', methods = ["POST"])
def add_event():
    event_name = request.form["name"]
    event_date = request.form["date"]
    guest_num = request.form["guests"]
    event_room = request.form["room"]
    event_description = request.form["description"]
    new_event = Event(event_name, event_date, guest_num, event_room, event_description, False, False)
    add_new_event(new_event)
    return render_template("index.html", title = "Home", events = events)