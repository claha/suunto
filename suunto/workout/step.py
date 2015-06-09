# Step
class Step(object):

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def generateCode(self, file, step):
        name = self.name
        duration = self.duration

        file.write('/* %s - %ss */\n' % (name, duration.s))
        if step == 0:
            file.write('if (STEP == %d) {\n' % (step))
        else:
            file.write('else if (STEP == %d) {\n' % (step))
        file.write('  prefix = "%s";\n' % (name))
        file.write('  RESULT = %d - STEPTIME;\n' % (duration.s))
        file.write('}\n')
        file.write('\n')

        return step+1
