from main import EventManager

# Function to load events from a text file
def load_events_from_file(filename):
    manager = EventManager()
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) == 5:
                    name, host, date, time, location = parts
                    manager.add_event(name, host, date, time, location)
        print("\n✅ Events loaded successfully from file.\n")
    except FileNotFoundError:
        print("⚠️ File not found. Starting with an empty event list.")
    return manager

# Function to print loaded events
def print_loaded_events(event_manager):
    print("\n📋 Loaded Events:")
    events = event_manager.list_events()
    if isinstance(events, list) and events:
        for event in events:
            print(f"✅ {event}")
    else:
        print("⚠️ No events found.")

# Function to display menu based on user role
def display_menu(role):
    print("\n📅 Event Manager")

    # Host
    if role in ["host"]:
        print("1. Add Event")
        print("2. Remove Event")
        print("3. Add Attendee")
        print("4. Remove Attendee")
        print("5. Check Event Details")
        print("6. List Events")

    # Attendee
    if role in ["attendee"]:
        if role == "attendee":
            print("7. Check Event Details")
            print("9. List Events")
        print("8. Check Time Conflict")
        print("10. Add Event")
        print("11. Remove Event")

    print("12. Exit")

# Main function to handle user interaction
def main():
    event_manager = load_events_from_file("text1.txt")
    print_loaded_events(event_manager)

    # Ask for user role
    role = ""
    while role not in ["host", "attendee"]:
        role = input("\nAre you a Host or Attendee? ").strip().lower()

    while True:
        display_menu(role)
        choice = input("Please input a number: ")
# add check date/time format, for example: if date doenst follow yyyy-mm-dd
# return Invalid date
# for time is HH:MM if it doesn't follow return Invalid time
        

        if choice == "1" and role == "host":
            name = input("Enter event name: ").strip()
            host = input("Enter host name: ").strip()
            date = input("Enter date (YYYY-MM-DD): ").strip()
            time = input("Enter time (HH:MM): ").strip()
            location = input("Enter location: ").strip()
            print(event_manager.add_event(name, host, date, time, location))

        elif choice == "2" and role == "host":
            name = input("Enter event name to remove: ").strip()
            if name in event_manager.events:
                print(event_manager.remove_event(name))
            else:
                print(f"⚠️ Event '{name}' not found.")

        elif choice == "3" and role == "host":
            event_name = input("Enter event name: ").strip()
            first_name = input("Enter attendee first name: ").strip()
            last_name = input("Enter attendee last name: ").strip()
            email = input("Enter attendee email: ").strip()
            if event_name in event_manager.events:
                print(event_manager.events[event_name].add_attendee(first_name, last_name, email))
            else:
                print("⚠️ Event not found.")

        elif choice == "4" and role == "host":
            event_name = input("Enter event name: ").strip()
            first_name = input("Enter attendee first name: ").strip()
            last_name = input("Enter attendee last name: ").strip()
            if event_name in event_manager.events:
                print(event_manager.events[event_name].remove_attendee(first_name, last_name))
            else:
                print("⚠️ Event not found.")

        elif choice == "5" and role == "host":
            event_name = input("Enter event name: ").strip()
            details = event_manager.get_event(event_name)
            if details:
                print("\n📌 Event Details:")
                for key, value in details.items():
                    print(f"{key}: {value}")
            else:
                print(f"⚠️ Event '{event_name}' not found.")

        elif choice == "6" and role == "host":
            print_loaded_events(event_manager)

        elif choice == "7" and role == "attendee":
            event_name = input("Enter event name: ").strip()
            details = event_manager.get_event(event_name)
            if details:
                print("\n📌 Event Details:")
                for key, value in details.items():
                    print(f"{key}: {value}")
            else:
                print(f"⚠️ Event '{event_name}' not found.")

        elif choice == "8" and role == "attendee":
            date = input("Enter event date (YYYY-MM-DD): ").strip()
            time = input("Enter event time (HH:MM): ").strip()
            conflict = event_manager.check_event_conflict(date, time)
            print("❌ Time conflict detected!" if conflict else "✅ No time conflicts.")

        elif choice == "9" and role == "attendee":
            print_loaded_events(event_manager)

        elif choice == "10" and role == "attendee":
            name = input("Enter event name: ").strip()
            host = input("Enter host name: ").strip()
            date = input("Enter date (YYYY-MM-DD): ").strip()
            time = input("Enter time (HH:MM): ").strip()
            location = input("Enter location: ").strip()
            print(event_manager.add_event(name, host, date, time, location))

        elif choice == "11" and role == "attendee":
            name = input("Enter event name to remove: ").strip()
            if name in event_manager.events:
                print(event_manager.remove_event(name))
            else:
                print(f"⚠️ Event '{name}' not found.")

        elif choice == "12":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("⚠️ Invalid choice or insufficient permissions.")

if __name__ == "__main__":
    main()

