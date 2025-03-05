import unittest
from main import Event, EventManager =


class TestEvent(unittest.TestCase):
# Set up test data
    def setUp(self):
        self.event = Event("Birthday Party", "Ken Smith", "2025-05-10", "18:00", "Los Angeles")

# Test event initalization
    def test_event_initialization(self):
        self.assertEqual(self.event.name, "Birthday Party")
        self.assertEqual(self.event.host_name, "Ken Smith")
        self.assertEqual(self.event.date, "2025-05-10")
        self.assertEqual(self.event.time, "18:00")
        self.assertEqual(self.event.location, "Los Angeles")
        self.assertEqual(self.event.attendees, {})

# Test add_attendee
    def test_add_attendee(self):
        result = self.event.add_attendee("John", "Jolie", "john.jolie@example.com")
        self.assertEqual(result, "John Jolie added to Birthday Party.")
        self.assertIn("John Jolie", self.event.attendees)

# Test remove_attendee
    def test_remove_attendee(self):
        self.event.add_attendee("John", "Jolie", "john.jolie@example.com")
        result = self.event.remove_attendee("John", "Jolie")
        self.assertEqual(result, "John Jolie removed from Birthday Party.")
        self.assertNotIn("John Jolie", self.event.attendees)

# Test get_attendee
    def test_get_attendees(self):
        self.event.add_attendee("John", "Jolie", "john.jolie@example.com")
        self.assertEqual(len(self.event.get_attendees()), 1)

class TestEventManager(unittest.TestCase):

# Set up test data for EventManager.
    def setUp(self):
        self.manager = EventManager()
        self.manager.add_event("Camping", "Roberts Cruz", "2025-07-15", "09:00", "Yellowstone Park")

# Test add_event
    def test_add_event(self):
        result = self.manager.add_event("Birthday Party", "Ken Smith", "2025-05-10", "18:00", "Los Angeles")
        self.assertEqual(result, "Successfully added event 'Birthday Party'.")
        self.assertIn("Birthday Party", self.manager.events)

# Test remove_event
    def test_remove_event(self):
        result = self.manager.remove_event("Camping")
        self.assertEqual(result, "Successfully removed event 'Camping'.")
        self.assertNotIn("Camping", self.manager.events)

# Test get_event
    def test_get_event(self):
        details = self.manager.get_event("Camping")
        self.assertEqual(details["Host"], "Roberts Cruz")

# Test list_events
    def test_list_events(self):
        self.manager.add_event("Birthday Party", "Ken Smith", "2025-05-10", "18:00", "Los Angeles")
        event_list = self.manager.list_events()
        self.assertIn("Camping", event_list)
        self.assertIn("Birthday Party", event_list)

# Test check_event_conflict
def test_check_event_conflict1(self):
    self.manager.add_event("Birthday Party", "Ken Smith", "2025-05-10", "18:00", "Los Angeles")
    self.assertTrue(self.manager.check_event_conflict("2025-05-10", "18:00"))

def test_check_event_conflict2(self):
    self.manager.add_event("Birthday Party", "Ken Smith", "2025-05-10", "18:00", "Los Angeles")
    self.assertFalse(self.manager.check_event_conflict("2025-05-11", "18:00"))
    self.assertFalse(self.manager.check_event_conflict("2025-05-10", "19:00"))

if __name__ == "__main__":
    unittest.main()
