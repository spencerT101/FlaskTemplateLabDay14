from modules.event import Event

event_1 = Event("Danny's Birthday", "14-04-2021", 50, "Grand Ballroom", "An elegant birthday bash!", True, True)
event_2 = Event("Buff Bash", '15-09-2021', 35, 'Snug Bar', 'Nudist Party', False, False)
event_3 = Event("Summer Party", '20-07-2021', 60, 'Secret Garden', 'Celebration of Summer', False, False)

events = [event_1, event_2, event_3]

def add_new_event(event):
    events.append(event)