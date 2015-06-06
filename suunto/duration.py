# Import
from .exceptions import SuuntoException

# Time
class Time(object):

    def __init__(self, h=None, m=None, s=None):
        if (h,m,s) == (None,None,None):
            raise SuuntoException('ERROR: Must provide h, m and/or s when creating Time object')
        self.s = (h*3600 if h else 0) + (m*60 if m else 0) + (s if s else 0)

    def __str__(self):
        return '<{0}: {1}s>'.format(self.__class__.__name__, self.s)

    def __repr__(self):
        return self.__str__()
