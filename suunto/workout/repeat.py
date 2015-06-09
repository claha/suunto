# Import
from .step import Step

# Repeat
class Repeat(object):

    def __init__(self, names, durations, count):
        self.steps = []
        for (name,duration) in zip(names,durations):
            self.steps.append(Step(name,duration))
        self.count = count

    def generateCode(self, file, step):
        count = self.count
        N = len(self.steps)
        for i in xrange(N):
            name = self.steps[i].name
            duration = self.steps[i].duration
            file.write('/* %s - %ss, STEP: %s */\n' % (name, duration.s, ','.join(map(str,range(step+i,step+i+N*count,N)))))
            if step == 0:
                file.write('if (Suunto.mod(STEP,%d) == %d && STEP > %d && STEP < %d) {\n' % (N,(i+step%N) % N,step-1,step+N*count))
            else:
                file.write('else if (Suunto.mod(STEP,%d) == %d && STEP > %d && STEP < %d) {\n' % (N,(i+step%N) % N,step-1,step+N*count))
            file.write('  prefix = "%s";\n' % (name))
            file.write('  RESULT = %d - STEPTIME;\n' % (duration.s))
            file.write('}\n')
            file.write('\n')

        return step + N*count
