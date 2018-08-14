""" Global variable store information """
DataBase = {}


def put(key, value):
    """
    Put a pair of key/value in the database
    """
    global DataBase
    DataBase[key] = value


def get(key):
    """
    Return the value associated to the key in the database
    """
    global DataBase
    return DataBase[key] if key in DataBase.keys() else None


def exists(key):
    """
    Return True if the key is in the database, False otherwise
    """
    global DataBase
    return key in DataBase


def delete(key):
    """
    Delete the key from the database
    """
    global DataBase
    if exists(key):
        del DataBase[key]
