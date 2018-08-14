""" Global variable store information """
DataBase = {}


def put(key, value):
    """
    Put a pair of key/value in the database
    """
    global DataBase
    DataBase[key] = value
    return value


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
        return True
    else:
        return False


def isValid(key):
    """
    Check value of key is int or float
    """
    global DataBase
    return (isinstance(DataBase[key], int) or
            isinstance(DataBase[key], float))


def incrby(key, delta):
    Database.setdefault(key, 0)
    try:
        Database[key] += delta
    except TypeError:
        raise ValueError('Incorrect value')
    return Database[key]


def incr(key):
    incrby(key, 1)
    return Database[key]

        
def isSet(key):
    """
    Check value of key is class Set or not
    """
    return isinstance(DataBase[key], set)


def sadd(key, value):
    """
    Add `value` to the set associated to `key`
    """
    if exists(key):
        if isSet(key):
            DataBase[key].add(value)
            return value
    else:
        DataBase[key] = {value}
    return value


def smembers(key):
    """
    Return the set values associated to `key`
    """
    if exists(key):
        return DataBase[key] if isSet(key) else None
    return None


def sunion(key1, key2):
    """
    Return all elements present accross both Sets
    """
    if exists(key1) and exists(key2):
        if isSet(key1) and isSet(key2):
            return DataBase[key1] | DataBase[key2]
    else:
        if exists(key1):
            return DataBase[key1] if isSet(key1) else None
        elif exists(key2):
            return DataBase[key2] if isSet(key2) else None
    return None


def sinter(key1, key2):
    """
    Return all elements shared between both Sets
    """
    if exists(key1) and exists(key2):
        if isSet(key1) and isSet(key2):
            return DataBase[key1] & DataBase[key2]
    return None


def srem(key, value):
    """
    Remove `value` in the set associated to `key`
    """
    if exists(key):
        if isSet(key):
            if value in DataBase[key]:
                DataBase[key].remove(value)
                return True
            else:
                return False
        else:
            return False
    else:
        return False
