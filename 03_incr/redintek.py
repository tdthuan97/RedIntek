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


def isValid(key):
    """
    Check value of key is int or float
    """
    global DataBase
    return (isinstance(DataBase[key], int) or
            isinstance(DataBase[key], float))


def incr(key):
    """
    Increment the value associated to `key` by one
    """
    global DataBase
    if exists(key):
        if isValid(key):
            DataBase[key] += 1
        else:
            raise ValueError('Incorrect value')
    else:
        DataBase[key] = 1


def incrby(key, delta):
    """
    Increment the value associated to `key` by `delta`
    """
    global DataBase
    if delta == 1:
        incr(key)
    elif exists(key):
        if isValid(key):
            DataBase[key] += delta
        else:
            raise ValueError('Incorrect value')
    else:
        DataBase[key] = 1 + delta
