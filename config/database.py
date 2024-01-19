from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database engine
engine = create_engine('sqlite:///db.sqlite', echo=True)  # echo=True will log SQL commands
engine_test = create_engine('sqlite:///db_test.sqlite', echo=True)  # echo=True will log SQL commands

# Session creation
Session = sessionmaker(bind=engine)
session = Session()

# Session creation for testing
Session_test = sessionmaker(bind=engine_test)
session_test = Session_test()

# Base class for declarative models
Base = declarative_base()

# Base class for declarative models for testing
Base_test = declarative_base()


