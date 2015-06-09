# Import
from ..exceptions import SuuntoException

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

    def __add__(self, other):
        if isinstance(other,Time):
            return Time(s=self.s+other.s)
        raise SuuntoException('ERROR: Cannot perform addition with {0} and {1}'.format(type(self), type(other)))

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other,int):
            return Time(s=other*self.s)
        raise SuuntoException('ERROR: Cannot perform multiplication with {0} and {1}'.format(type(self), type(other)))

    def __rmul__(self,other):
        return self.__mul__(other)
