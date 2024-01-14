from config.app import app
from contacts.controllers import *


@app.get("/contacts")
def get_contacts():
    return get_all_contacts()


@app.get("/contacts/{id}")
def get_one_contact(id):
    return get_this_contact(id)


@app.post("/contacts")
def add_contact(contact):
    return create_contact(contact)


@app.delete("/contacts/{id}")
def delete_contact(id):
    return delete_this_contact(id)


@app.put("/contacts/{id}")
def update_contact(id, contact):
    return update_this_contact(id, contact)
