# Import
from ..exceptions import SuuntoDurationException
from .duration import Duration

# Time
class Time(Duration):

    def __init__(self, h=None, m=None, s=None):
        if (h,m,s) == (None,None,None):
            raise SuuntoDurationException('ERROR: Must provide h, m and/or s when creating Time object')
        self.s = (h*3600 if h else 0) + (m*60 if m else 0) + (s if s else 0)

    def getDuration(self):
        return self.s
        
    def getUnit(self):
        return 's'

    def generateResult(self):
        return '%d - STEPTIME' % (self.s)
