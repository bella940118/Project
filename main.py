

# Initializes an Event object.
class Event:
    def __init__(self, name: str, host_name: str, date: str, time: str, location: str):
        self.name = name
        self.host_name = host_name
        self.date = date
        self.time = time
        self.location = location
        self.attendees = {}

# Adds an attendee to the event.
    def add_attendee(self, first_name: str, last_name: str, email: str) -> str:
        full_name = f"{first_name} {last_name}"
        if full_name not in self.attendees:
            self.attendees[full_name] = {"First Name": first_name, "Last Name": last_name, "Email": email}
            return f"{full_name} added to {self.name}."
        return f"{full_name} is already attending."

# Removes an attendee from the event.
    def remove_attendee(self, first_name: str, last_name: str) -> str:
        full_name = f"{first_name} {last_name}"
        if full_name in self.attendees:
            del self.attendees[full_name]
            return f"{full_name} removed from {self.name}."
        return f"{full_name} was not found in {self.name}."

#Returns a dictionary of attendees.
    def get_attendees(self) -> dict:
        return self.attendees if self.attendees else "No attendees yet."

# Returns event details.
    def get_event_details(self) -> dict:
        return {
            "Event Name": self.name,
            "Host": self.host_name,
            "Date": self.date,
            "Time": self.time,
            "Location": self.location,
            "Attendees": self.attendees
        }


# Initializes an EventManager instance to manage multiple events.
class EventManager:
    def __init__(self):
        self.events = {}

# Adds a new event.
    def add_event(self, name: str, host_name: str, date: str, time: str, location: str) -> str:

        if name not in self.events:
            self.events[name] = Event(name, host_name, date, time, location)
            return f"Successfully added event '{name}'."
        return f"Event '{name}' already exists."

# Removes an event.
    def remove_event(self, name: str) -> str:
        if name in self.events:
            del self.events[name]
            return f"Successfully removed event '{name}'."
        return f"Event '{name}' not found."

# Retrieves details of a specific event.
    def get_event(self, name: str) -> dict:
        if name in self.events:
            return self.events[name].get_event_details()
        return {}

# Lists all events
    def list_events(self) -> list:

        return list(self.events.keys()) if self.events else "No events available."

#  Checks if there is a conflict with an existing event at the same date and time.
    def check_event_conflict(self, date: str, time: str) -> bool:
        for event in self.events.values():
            if event.date == date and event.time == time:
                return True
        return False