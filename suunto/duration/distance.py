# Import
from ..exceptions import SuuntoDurationException
from .duration import Duration

# Distance
class Distance(Duration):

    def __init__(self, km=None, m=None):
        if (km,m) == (None,None):
            raise SuuntoDurationException('ERROR: Must provide km and/or m when creating Distance object')
        self.m = (km*1000 if km else 0) + (m if m else 0)

    def getDuration(self):
        return self.m

    def getUnit(self):
        return 'm'

    def generateResult(self):
        return '%d - STEPDIST' % (self.m)
