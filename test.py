import unittest
from main import Event


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.event = Event("Coding Workshop", "Professor B", "2025-03-10", "10:00AM", "Room 101")

# Test add attendees
    def test_add_attendee(self):
        result = self.event.add_attendee("John", "Doe", "johndoe@example.com")
        self.assertEqual(result, "John Doe added to Coding Workshop.")
        self.assertIn("John Doe", self.event.attendees)

# Test remove attendees
    def test_remove_attendee(self):
        result = self.event.remove_attendee("John", "Doe")
        self.assertEqual(result, "John Doe removed from Coding Workshop.")
        self.assertIn("John Doe", self.event.attendees)


if __name__ == '__main__':
    unittest.main()


