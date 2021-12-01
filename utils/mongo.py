import os

from mongoengine import connect


def get_db_connection_url() -> str:
    url = "mongodb+srv://test:{}@cluster0.b1gbm.mongodb.net/{}?retryWrites=true&w=majority".format(
        os.environ["PASS"], os.environ["DB"]
    )
    return url


def db_config():
    try:
        uri: str = get_db_connection_url()
        connect(host=uri)
    except KeyError:
        connect("mongoenginetest", host="mongomock://localhost")
