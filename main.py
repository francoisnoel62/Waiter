from config.app import app
import contacts.urls


@app.route("/")
def hello():
    return "Hello, World from Waiter!"


if __name__ == "__main__":
    app.run()
