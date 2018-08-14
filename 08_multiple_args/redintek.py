""" Global variable store information """
DataBase = {}


def put(key, *values):
    """
    Put a pair of key/value in the database
    """
    global DataBase
    for value in values:
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


def delete(*keys):
    """
    Delete the key from the database
    """
    global DataBase
    sizeBegin = len(DataBase)
    for key in keys:
        if exists(key):
            del DataBase[key]
    return sizeBegin - len(DataBase)


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
    return DataBase[key]


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
    return DataBase[key]


def isSet(key):
    """
    Check value of key is class Set or not
    """
    return isinstance(DataBase[key], set)


def sadd(key, *values):
    """
    Add `value` to the set associated to `key`
    """
    if exists(key):
        sizeBegin = len(DataBase[key]) if isSet(key) else 0
    else:
        sizeBegin = 0
    for value in values:
        if exists(key):
            if isSet(key):
                DataBase[key].add(value)
        else:
            DataBase[key] = {value}
    return len(DataBase[key]) - sizeBegin


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


def srem(key, *values):
    """
    Remove `value` in the set associated to `key`
    """
    if exists(key):
        sizeBegin = len(DataBase[key]) if isSet(key) else 0
        if isSet(key):
            for value in values:
                if value in DataBase[key]:
                    DataBase[key].remove(value)
            sizeAfter = len(DataBase[key])
        else:
            sizeAfter = 0
    else:
        sizeBegin = 0
        sizeAfter = 0
    return sizeBegin - sizeAfter
