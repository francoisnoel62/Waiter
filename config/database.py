from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database engine
engine = create_engine('sqlite:///db.sqlite', echo=True)  # echo=True will log SQL commands

# Session creation
Session = sessionmaker(bind=engine)
session = Session()

# Base class for declarative models
Base = declarative_base()
