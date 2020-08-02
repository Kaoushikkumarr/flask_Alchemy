# creating models data here.

from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(object):  # creating Result() class.
    __tablename__ = 'results'  # same table name in Database

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):  # initialization of variables.
        self.url: str = url
        self.result_all: JSON = result_all
        self.result_no_stop_words: JSON = result_no_stop_words

    def __repr__(self):  # representing the object of db columns
        return '<id {}>'.format(self.id)
