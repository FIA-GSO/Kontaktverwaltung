from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///contacts.db')
Session = sessionmaker(bind=engine)


class ContactModel(Base):
    __tablename__ = 'contacts'

    uuid = Column(String, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)


# create database and tables
Base.metadata.create_all(engine)
