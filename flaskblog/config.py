import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY','123456789')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI','sqlite:///site.db')
    