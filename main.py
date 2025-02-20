
class Event:
    def __init__(self, host_name, data, time, location):
        self.host_name = host_name
        self.data = data
        self.time = time
        self.location = location
        self.attendees = []


    def __str__(self):
        return f'{self.host_name}, {self.data}, {self.time}, {self.location}, {self.attendees}'

    def __repr__(self):
        return f'{self.host_name}, {self.data}, {self.time}, {self.location}, {self.attendees}'

    def add_attendee(self, attendee_first_name: str, attendee_last_name:str):
        self.attendees.append((attendee_first_name, attendee_last_name))

    def remove_attendee(self, attendee_name):
        self.attendees.remove(attendee_name)

    def get_attendees(self):
        return self.attendees

    def get_event_details(self):
        return {
            'Host': self.host_name,
            'Data': self.data,
            'Time': self.time,
            'Location': self.location,
        }
