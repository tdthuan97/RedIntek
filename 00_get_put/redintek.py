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
