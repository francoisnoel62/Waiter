from config.app import app
from contacts.controllers import list_contacts


# Register the route and associate it with the list_contacts function
@app.route("/contacts")
def contacts_route():
    return list_contacts()
