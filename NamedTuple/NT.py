from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'is_done', 'date'])
Task.__new__.__defaults__ = (None, None, False, None)
