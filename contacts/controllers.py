import logging

from config.customs_exceptions import ObjectDoesNotExistsException
from config.database import session
from contacts.models import Contact
from utils.json import to_json


def get_all_contacts():
    contacts_data = session.query(Contact).all()
    return to_json(contacts_data)


def get_this_contact(id):
    contact = session.query(Contact).filter_by(id=id).first()
    if not contact:
        raise ObjectDoesNotExistsException()

    return to_json(contact)


def create_contact(contact):
    new_contact = Contact(**contact)
    session.add(new_contact)
    session.commit()
    return to_json(new_contact)


def delete_this_contact(id):
    try:
        contact = session.query(Contact).filter_by(id=id).first()
        session.delete(contact)
        session.commit()
        return get_all_contacts()
    except Exception as e:
        logging.error(e)
        return "Contact not found"



def update_this_contact(id, contact):
    this_contact = session.query(Contact).filter_by(id=id).first()
    for key in ['name', 'email', 'phone']:
        if key in contact:
            setattr(this_contact, key, contact[key])
    session.commit()
    return to_json(this_contact)
