
class Event:
    def __init__(self, name, host_name, data, time, location):
        self.name = name
        self.host_name = host_name
        self.data = data
        self.time = time
        self.location = location
        self.attendees = {}


    def __str__(self):
        return f'{self.name},{self.host_name}, {self.data}, {self.time}, {self.location}, {self.attendees}'

    def __repr__(self):
        return f'{self.name},{self.host_name}, {self.data}, {self.time}, {self.location}, {self.attendees}'



    def add_attendee(self, first_name: str, last_name: str, email: str):
        self.full_name = f"{first_name} {last_name}"
        if self.full_name not in self.attendees:
            self.attendees[self.full_name] = {"First Name": first_name, "Last Name": last_name, "Email": email}
            return f"{self.full_name} added to {self.name}."
        return f"{self.full_name} is already attending."


    def remove_attendee(self, first_name: str, last_name: str):
        self.full_name = f"{first_name} {last_name}"
        if self.full_name in self.attendees:
            del self.attendees[self.full_name]
            return f"{self.full_name} removed from {self.name}."
        return f"{self.full_name} removed from {self.name}."

    def get_attendees(self):
        return self.attendees if self.attendees else "No attendees yet."

    def get_event_details(self):
        return {
            'Host': self.host_name,
            'Data': self.data,
            'Time': self.time,
            'Location': self.location,
        }

class EventManager:
    def __init__(self):
        self.events = []

    def add_event(self, name: str, data: str, time: str, location: str):
        new_event = Event(name, data, time, location)
        self.events.append(new_event)
        return f'Successfully added {name} event', new_event

    def remove_event(self, name: str):
        for event in self.events:
            if event.name == name:
                self.events.remove(event)
                return f'Successfully removed {name} event', event
            return f'Failed to find {name} event', None


