from config.app import app
from contacts.controllers import get_all_contacts, get_this_contact, create_contact


# Register the route and associate it with the list_contacts function
@app.get("/contacts")
def get_contacts():
    return get_all_contacts()


@app.get("/contacts/{id}")
def get_one_contact(id):
    return get_this_contact(id)


@app.post("/contact")
def add_contact(contact):
    return create_contact(contact)
