from datetime import datetime
""" Mini-serializer"""


def to_json(obj):
    """ Function to serialize datetime object to string
    datetime -> str"""
    if isinstance(obj, datetime):
        return datetime.isoformat(obj)
    raise TypeError(repr(obj) + ' is not JSON serializable')
