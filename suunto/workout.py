# Import
import sys
from .duration import Time

# Workout
class Workout(object):

    def __init__(self):
        self.steps = []

    # TODO: check that len(name) <= 6 chars
    def addStep(self, name, duration):
        self.steps.append((name, duration))

    # TODO: check that len(name) <= 6 - len(repeat)
    def addRepeat(self, names, durations, repeat):
        for r in xrange(repeat):
            for (name,duration) in zip(names,durations):
                self.addStep(name + str(r+1), duration)

    def generateCode(self, filename=None):
        
        # Open
        if not filename is None:
            f = open(filename, 'w')
        else:
            f = sys.stdout

        def wr(txt):
            f.write(txt + '\n')

        # Generate
        wr('if (SUUNTO_DURATION == 0) {')
        wr('  prefix = "%s";' % (self.steps[0][0]))
        wr('  RESULT = %d;' % (self.steps[0][1].s))
        wr('  STEP = 0;')
        wr('  ELAPSEDTIME = 0;')
        wr('}')
        wr('')

        for i,step in enumerate(self.steps):
            if i == 0:
                wr('if (STEP == %d && SUUNTO_DURATION > 0) {' % (i))
            else:
                wr('if (STEP == %d) {' % (i))
            wr('  prefix = "%s";' % (step[0]))
            wr('  RESULT = %d - (SUUNTO_DURATION - ELAPSEDTIME);' % (step[1].s))

            if i == len(self.steps) - 1:
                wr('  if (RESULT <= 0) {')
            else:
                wr('  if (RESULT == 0) {')
                wr('    STEP = STEP + 1;')
                wr('    ELAPSEDTIME = SUUNTO_DURATION;')
            wr('    Suunto.alarmBeep();')
            wr('  }')
            wr('}')
            wr('')

        # Close
        if not filename is None:
            f.close()

