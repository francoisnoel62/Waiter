import os
import sqlite3
import unittest
from faker import Faker

fake = Faker()


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db_file = 'test_database.db'
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE contacts (name TEXT, phone TEXT, email TEXT)')

    def tearDown(self):
        self.connection.close()
        os.remove(self.db_file)

    def test_insert_and_retrieve_data(self):
        for i in range(5):
            fake_name = fake.name()
            fake_phone = fake.phone_number()
            fake_email = fake.email()

            self.cursor.execute(
                "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (fake_name, fake_phone, fake_email))

            self.connection.commit()


if __name__ == '__main__':
    unittest.main()
