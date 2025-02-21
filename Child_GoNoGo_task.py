# imports
from psychopy import visual, sound, event, core, gui
import os
from helper import generate_trials, check_paths
import time

# this task could be basically the same as the left right task but where they only go on green and not yellow

##### MAKE SURE ALL THE PIECES ARE IN THE RIGHT PLACE #####
current_directory = os.path.dirname(os.path.abspath(__file__))
check_paths(current_directory)