from contacts.models import Contact
from utils.json import to_json
from config.database import get_contacts


def list_contacts():
    # Fetch contacts and convert them to Contact objects
    contacts_data = get_contacts()
    contacts = [Contact(*data) for data in contacts_data]

    # Use the to_json utility to serialize the contacts
    return to_json(contacts)



