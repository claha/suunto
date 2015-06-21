# Import
from suunto import Workout
from suunto import Time
from suunto import Distance
from suunto.constants import *

# Define workout
# Warmup - 10min
# For 5 rounds repeat
#  Work - 100M
#  Rest - 30s
# Cooldown - 5min
#
# Use the predefined times/distances or create your own using:
# Time(h=hours,m=minutes,s=seconds)/Distance(km=kilometers,m=meters) 
# at least one of the arguments (h,m,s)/(km,m) is required
workout = Workout()
workout.addStep('WARM',T20M + 2*T10M*2)
workout.addRepeat(['WORK','REST'], [3*D100M + D100M, T30S], 5)
workout.addStep('COOL', T10M)

# Generate code to file
# workout.generateCode('myworkout.c')
# Generate code to stdout
workout.generateCode()

