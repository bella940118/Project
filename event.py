import main

# Dictionary to store event with event schedule
event_schedule = {}

def add_event(name, date, time, location):
    event = main.Event(name, date, time, location)
    event_schedule[name] = event

def remove_event(name):
    if name in event_schedule:
        del event_schedule[name]

def retrieve_events():
    for event in event_schedule.values():
        print(event.get_details())
