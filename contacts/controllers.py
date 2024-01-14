import logging

from config.database import session
from contacts.models import Contact
from utils.json import to_json


def get_all_contacts():
    contacts_data = session.query(Contact).all()
    return to_json(contacts_data)


def get_this_contact(id):
    contact = session.query(Contact).filter_by(id=id).first()
    return to_json(contact)


def create_contact(contact):
    new_contact = Contact(**contact)
    session.add(new_contact)
    session.commit()
    return to_json(new_contact)


def delete_this_contact(id):
    contact = session.query(Contact).filter_by(id=id).first()
    session.delete(contact)
    session.commit()
    return get_all_contacts()


def update_this_contact(id, contact):
    this_contact = session.query(Contact).filter_by(id=id).first()
    for key in ['name', 'email', 'phone']:
        if key in contact:
            setattr(this_contact, key, contact[key])
    session.commit()
    return to_json(this_contact)
