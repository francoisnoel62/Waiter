# Waiter

## Overview
'Waiter' is a minimalistic Python framework designed for learning purposes. It is aimed at those who wish to create APIs quickly and easily. This framework simplifies the development process, making it ideal for beginners and for rapidly prototyping applications.

## Key Components
1. **main.py**: Initializes the application and orchestrates interactions between modules.
2. **json.py**: Manages JSON data parsing and formatting.
3. **urls.py**: Configures URL routes, mapping them to specific functions or controllers.
4. **models.py**: Defines database models, including structure and relationships.
5. **controllers.py**: Handles HTTP requests and application logic.
6. **database.py**: Manages database connections and operations.
7. **app.py**: Sets up the web application framework and environment.

## Dependencies
- `greenlet==3.0.3`
- `SQLAlchemy==2.0.25`
- `typing_extensions==4.9.0`

Install these dependencies to ensure the application runs correctly.

## Usage
Run `main.py` to start the application. Ensure all dependencies are installed and the database is properly configured as per `models.py` and `database.py`.

## License
This project is licensed under the MIT License. See `LICENSE` for more information.

## Contact
If you have any questions or concerns, please feel free to contact me at francoisnoel62@gmail.com

## Acknowledgements
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [Python Documentation](https://docs.python.org/3/)
- [JSON Documentation](https://www.json.org/json-en.html)
- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)