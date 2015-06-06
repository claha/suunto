# Import
from suunto import Workout
from suunto import Time
from suunto.constants import *

# Define workout
# Warmup - 10min
# For 5 rounds repeat
#  Work - 30s
#  Rest - 30s
# Cooldown - 5min
#
# Use the predefined times or create your own using:
# Time(h=hours,m=minutes,s=seconds), 
# at least one of the arguments (h,m,s) is required
workout = Workout()
workout.addStep('WARM', T10M)
workout.addRepeat(['WORK','REST'], [T30S, T30S], 5)
workout.addStep('COOL', T5M)

# Generate code to file
workout.generateCode('myworkout.c')
# Generate code to stdout
workout.generateCode()

