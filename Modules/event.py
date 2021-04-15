class Event:

    def __init__(self, event_name, date, num_guest, room_loc, description, confirmed, recurring):
        self.date = date
        self.event_name = event_name
        self.num_guest = num_guest
        self.room_loc = room_loc
        self.description = description
        self.confirmed = confirmed
        self.recurring = recurring