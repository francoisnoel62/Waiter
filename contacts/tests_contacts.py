import json
import unittest
from unittest.mock import patch

from contacts.controllers import get_all_contacts, get_this_contact
from contacts.models import Contact


class TestContactsController(unittest.TestCase):
    @patch('contacts.controllers.session')
    def test_get_all_contacts(self, mock_session):
        # Setup mock data
        mock_contacts = [Contact(id=5, name="John Doe", email="john@example.com", phone="1234567890"),
                         Contact(id=6, name="Jane Doe", email="test@test.ch", phone="0987654321")]
        mock_session.query.return_value.all.return_value = mock_contacts

        # Call the method
        result_json = get_all_contacts()
        result = json.loads(result_json)

        # Assert the results
        self.assertIsNotNone(result)
        self.assertEqual(2, len(result))

        # Assert the data
        self.assertEqual(5, result[0]['id'])
        self.assertEqual("John Doe", result[0]['name'])
        self.assertEqual("john@example.com", result[0]['email'])
        self.assertEqual("1234567890", result[0]['phone'])

        # Assert the data are of JSON type
        self.assertIsInstance(result_json, str)

    @patch('contacts.controllers.session')
    def test_get_one_contact(self, mock_session):
        # Mocking a single contact
        mock_contact = Contact(id=1, name="John Doe", email="john@example.com", phone="1234567890")

        # Set up the mock to return the contact when queried with specific ID
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_contact

        # Call the method with the ID of the mocked contact
        result_json = get_this_contact(1)
        result = json.loads(result_json)

        print(result)

        # Assert the results
        self.assertIsNotNone(result)
        self.assertEqual(result[0]['name'], "John Doe")
        self.assertEqual(result[0]['email'], "john@example.com")
        self.assertEqual(result[0]['phone'], "1234567890")


if __name__ == '__main__':
    unittest.main()
