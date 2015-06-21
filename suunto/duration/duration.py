# Import
from ..exceptions import SuuntoDurationException

# Duration
class Duration(object):

    def __str__(self):
        return '<{0}: {1}{2}>'.format(self.__class__.__name__, self.getDuration(), self.getUnit())

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other,self.__class__):
            return self.__class__(**{self.getUnit() : self.getDuration() + other.getDuration()})
        raise SuuntoException('ERROR: Cannot perform addition with {0} and {1}'.format(type(self), type(other)))

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other,int):
            return  self.__class__(**{self.getUnit() : other * self.getDuration()})
        raise SuuntoException('ERROR: Cannot perform multiplication with {0} and {1}'.format(type(self), type(other)))

    def __rmul__(self,other):
        return self.__mul__(other)
        
    # Subclass should implement the following methods
    # def getDuration(self):
    # def getUnit(self):
    # def generateResult(self):