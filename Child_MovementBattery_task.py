##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
########                 This task is UNFINISHED pending meeting with                 ########
########                   colleagues regarding best steps forward.                   ########
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################

raise ValueError('ERROR: This task is UNFINISHED pending meeting with colleagues regarding best steps forward.')

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

##### Get runtime variables with the psychopy GUI#####
def get_runtime_vars(vars_to_get,order,exp_version="experiment_code_for_reference"):
    infoDlg = gui.DlgFromDict(dictionary=vars_to_get, title=exp_version, order=order)
    if infoDlg.OK:
        return vars_to_get
    else: 
        print('User Cancelled')
order =  ['subj_code','seed','num_trials']
runtime_vars = get_runtime_vars({'subj_code':'S001', 'seed':1, 'num_trials':50}, order)

##### Set up psychopy features for the task #####
# timer
timer = core.Clock()
reaction_times = []
# set window paramaters
win = visual.Window([1000,800], color='lightgray', units='pix', checkTiming=False)
# preopen all the important stimuli
#  FIGURE STIMULI
figure = visual.ImageStim(win, image=f'{current_directory}/stimuli/LR_stimuli/LR_figure.png', pos=[0,0], size=[383.7,700])
#  HAND STIMULI
hand_l_plan = visual.ImageStim(win, image=f'{current_directory}/stimuli/LR_stimuli/LR_hand_l_plan.png', pos=[0,0], size=[383.7,700])
hand_r_plan = visual.ImageStim(win, image=f'{current_directory}/stimuli/LR_stimuli/LR_hand_r_plan.png', pos=[0,0], size=[383.7,700])
hand_l_exec = visual.ImageStim(win, image=f'{current_directory}/stimuli/LR_stimuli/LR_hand_l_exec.png', pos=[0,0], size=[383.7,700])
hand_r_exec = visual.ImageStim(win, image=f'{current_directory}/stimuli/LR_stimuli/LR_hand_r_exec.png', pos=[0,0], size=[383.7,700])
#  FOOT STIMULI
foot_l_plan = visual.ImageStim(win, image=f'{current_directory}/stimuli/LR_stimuli/LR_foot_l_plan.png', pos=[0,0], size=[383.7,700])
foot_r_plan = visual.ImageStim(win, image=f'{current_directory}/stimuli/LR_stimuli/LR_foot_r_plan.png', pos=[0,0], size=[383.7,700])
foot_l_exec = visual.ImageStim(win, image=f'{current_directory}/stimuli/LR_stimuli/LR_foot_l_exec.png', pos=[0,0], size=[383.7,700])
foot_r_exec = visual.ImageStim(win, image=f'{current_directory}/stimuli/LR_stimuli/LR_foot_r_exec.png', pos=[0,0], size=[383.7,700])
#  MOUTH STIMULI
mouth_plan = visual.ImageStim(win, image=f'{current_directory}/stimuli/LR_stimuli/LR_mouth_plan.png', pos=[0,0], size=[383.7,700])
mouth_exec = visual.ImageStim(win, image=f'{current_directory}/stimuli/LR_stimuli/LR_mouth_exec.png', pos=[0,0], size=[383.7,700])

stimuli_dict = {
    'hand_l_plan': hand_l_plan,'hand_r_plan': hand_r_plan,
    'hand_l_exec': hand_l_exec,'hand_r_exec': hand_r_exec,
    'foot_l_plan': foot_l_plan,'foot_r_plan': foot_r_plan,
    'foot_l_exec': foot_l_exec,'foot_r_exec': foot_r_exec,
    'mouth_plan': mouth_plan,'mouth_exec': mouth_exec
}

#  SOUND STIMULI
correct_sound = sound.Sound(f'{current_directory}/stimuli/zapsplat_multimedia_game_sound_short_beep_earn_point_pick_up_item_001_78373.wav')
incorrect_sound = sound.Sound(f'{current_directory}/stimuli/zapsplat_multimedia_game_sound_short_high_pitched_buzzer_78377.wav')

# Gordon et al. 2023
''' 
Movement task battery
A block design was adapted from the motor task in ref. 31. In each run, the participant was presented with visual cues 
that directed them to perform one of five specific movements. Each block started with a 2.2-s cue indicating which 
movement was to be made. After this cue, a centrally presented caret replaced the instruction and flickered once every 
1.1s (without temporal jittering). Each time the caret flickered, participants executed the proper movement. Twelve 
movements were made per block. Each block lasted 15.4s, and each task run consisted of 2 blocks of each type of 
movement as well as 3 blocks of resting fixation. Movements conducted within each run were as follows:

Run type 1: Close left (L) hand/Close right (R) hand/Flex L foot/Move tongue L and R (participant 1: 24 runs; 
participant 2: 20 runs).

Run type 2: Flex L elbow/Flex R elbow/Flex L wrist/Flex R wrist/Lift bilateral shoulders (participant 1: 10 runs; 
participant 2: 11 runs).

Run type 3: Flex L gluteus/Flex R gluteus/Tense abdomen/Open and close mouth/Swallow (participant 1: 10 runs; 
participant 2: 11 runs).

Run type 4: Flex L ankle/Flex R ankle/Bend L knee/Bend R knee/Flex bilateral toes (participant 1: 10 runs; 
participant 2: 11 runs).

Run type 5: Lift L eyebrow/Lift R eyebrow/Wink L eyelid/Wink R eyelid/Flare nostrils (participant 1: 10 runs; 
participant 2: 11 runs).
'''
