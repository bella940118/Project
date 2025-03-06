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

from main import *
def event_conflict(A:Event,B:Event):
    if A.location == B.location and A.time == B.time:
        return True

def personal_conflict (A:Event,B:Event):
    # we should potentially store this in a dictionary where the keys are the attendee names are
    # the keys and they determine which events the person has scheduled, and we can create a
    # function that can determine whether they have any conflicting event at that time.

def check_for_conflicts(A:Event,all_events:list[Event]):
    for n in range(len(all_events)):
        x= event_conflict(A,all_events[n])
        if x== True:
            return "events conflicts with other event"
            break
