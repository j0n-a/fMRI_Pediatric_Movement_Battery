# imports
from psychopy import visual, sound, event, core, gui
import os
from helper import generate_trials, check_paths
import time

"""
This experiment was created partly for UCSD's COGS 219 (WI25) Final Project using PsychoPy (v2024.1.1).

Updated 03/11/2025 by JA 
"""

##### MAKE SURE ALL THE PIECES ARE IN THE RIGHT PLACE #####
current_directory = os.path.dirname(os.path.abspath(__file__))
check_paths(current_directory, task='MovementBattery')

