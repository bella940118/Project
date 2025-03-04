import unittest
from main import Event


class MyTestCase(unittest.TestCase):

# Test add attendees
    def test_add_attendee1(self):
        event = Event("Coding Workshop", "2025-03-10", "10:00AM", "Room 101")
        add = event.add_attendee("Tom", "Smith")
        result = event.get_attendees()
        self.assertEqual(result, [('Tom', 'Smith')])

    def test_add_attendee2(self):
        event = Event("Coding Workshop", "2025-03-10", "10:00AM", "Room 101")
        add = event.add_attendee("Ken", "Smith")
        result = event.get_attendees()
        self.assertEqual(result, [('Ken', 'Smith')])

    def test_get_event_details(self):
        event= Event("Coding Workshop", "2025-03-10","10:00AM","Room 101")
        result= event.get_event_details()
        self.assertEqual(result, {'Codding Workshop','2025-03-10','10:00AM','Room 101'})

 
if __name__ == '__main__':
    unittest.main()


