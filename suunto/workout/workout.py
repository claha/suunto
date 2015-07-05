# Import
import sys
from .step import Step
from .repeat import Repeat

# Workout
class Workout(object):

    def __init__(self):
        self.workout = []
        self.steps = []
        self.postfixEnabled = True

    # TODO: check that len(name) <= 6
    def addStep(self, name, duration):
        self.workout.append(Step(name, duration))

    # TODO: check that len(name) <= 6 - len(count)
    def addRepeat(self, names, durations, count):
        self.workout.append(Repeat(names, durations, count))

    def generateCode(self, filename=None):

        # Open
        if not filename is None:
            file = open(filename, 'w')
        else:
            file = sys.stdout

        def wr(txt):
            file.write(txt + '\n')

        # Generate
        wr('/* Reset */')
        wr('if (SUUNTO_DURATION == 0) {')
        wr('  STEP = 0;')
        wr('  PREVSTEP = 0;')
        wr('  STEPSTARTTIME = 0;')
        wr('  STEPSTARTDIST = 0;')
        wr('  STEPTIME = 0;')
        wr('  STEPDIST = 0;')
        wr('}')
        wr('')

        wr('/* Next step */')
        wr('if (STEP != PREVSTEP) {')
        wr('  Suunto.alarmBeep();')
        wr('  STEPSTARTTIME = SUUNTO_DURATION;')
        wr('  STEPSTARTDIST = SUUNTO_DISTANCE*1000;')
        wr('}')
        wr('')
        
        wr('/* Update */')
        wr('PREVSTEP = STEP;')
        wr('STEPTIME = SUUNTO_DURATION - STEPSTARTTIME;')
        wr('STEPDIST = SUUNTO_DISTANCE*1000 - STEPSTARTDIST;')
        wr('')

        step = 0
        for w in self.workout:
            step = w.generateCode(file,step,self.postfixEnabled)

        wr('/* Check result */')
        wr('if ( RESULT <= 0 ) {')
        wr('  STEP = STEP + 1;')
        wr('  RESULT = 0;')
        wr('}')

        # Close
        if not filename is None:
            file.close()

