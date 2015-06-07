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
        wr('  STEP = 0;')
        wr('  PREVSTEPSDURATION = 0;')
        wr('}')
        wr('')
        
        for i,step in enumerate(self.steps):
            wr('/* %s - %ss */' % (step[0], step[1].s))
            wr('if (STEP == %d) {' % (i))
            wr('  prefix = "%s";' % (step[0]))
            wr('  RESULT = %d - (SUUNTO_DURATION - PREVSTEPSDURATION);' % (step[1].s))

            if i == len(self.steps) - 1:
                wr('  if (RESULT <= 0) {')
            else:
                wr('  if (RESULT == 0) {')
                wr('    STEP = %d; /* %s */' % (i+1,self.steps[i+1][0]))
                wr('    PREVSTEPSDURATION = SUUNTO_DURATION;')
            wr('    Suunto.alarmBeep();')
            wr('  }')
            wr('}')
            wr('')

        # Close
        if not filename is None:
            f.close()

