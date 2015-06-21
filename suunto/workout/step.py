# Step
class Step(object):

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        
    def generateHeader(self):
        return '/* %s - %s */\n' % (self.name, self.duration)

    def generateCode(self, file, step):
        file.write(self.generateHeader())
        if step > 0:
            file.write('else ')
        file.write('if (STEP == %d) {\n' % (step))
        file.write('  prefix = "%s";\n' % (self.name))
        file.write('  RESULT = %s;\n' % (self.duration.generateResult()))
        file.write('  postfix = "%s";\n' % (self.duration.getUnit()))
        file.write('}\n\n')

        return step+1
