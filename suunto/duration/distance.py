# Import
from ..exceptions import SuuntoException

# Distance
# TODO: Distance should inherit from a Duration-class
class Distance(object):

    def __init__(self, km=None, m=None):
        if (km,m) == (None,None):
            raise SuuntoException('ERROR: Must provide km and/or m when creating Distance object')
        self.m = (km*1000 if km else 0) + (m if m else 0)

    def __str__(self):
        return '<{0}: {1}m>'.format(self.__class__.__name__, self.m)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other,Distance):
            return Distance(m=self.m+other.m)
        raise SuuntoException('ERROR: Cannot perform addition with {0} and {1}'.format(type(self), type(other)))

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other,int):
            return Distance(m=other*self.m)
        raise SuuntoException('ERROR: Cannot perform multiplication with {0} and {1}'.format(type(self), type(other)))

    def __rmul__(self,other):
        return self.__mul__(other)
        
    def generateResult(self):
        return '  RESULT = %d - STEPDIST;\n' % (self.m)
