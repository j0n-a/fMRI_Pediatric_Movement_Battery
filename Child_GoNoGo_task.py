# imports
from psychopy import visual, sound, event, core, gui
import os
from helper import generate_trials, check_paths
import time

# this task could be basically the same as the left right task but where they only go on green and not yellow

##### MAKE SURE ALL THE PIECES ARE IN THE RIGHT PLACE #####
current_directory = os.path.dirname(os.path.abspath(__file__))
check_paths(current_directory)

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
figure = visual.ImageStim(win, image=f'{current_directory}/stimuli/figure.png', pos=[0,0], size=[383.7,700])
#  HAND STIMULI
hand_l_plan = visual.ImageStim(win, image=f'{current_directory}/stimuli/hand_l_plan.png', pos=[0,0], size=[383.7,700])
hand_r_plan = visual.ImageStim(win, image=f'{current_directory}/stimuli/hand_r_plan.png', pos=[0,0], size=[383.7,700])
hand_l_exec = visual.ImageStim(win, image=f'{current_directory}/stimuli/hand_l_exec.png', pos=[0,0], size=[383.7,700])
hand_r_exec = visual.ImageStim(win, image=f'{current_directory}/stimuli/hand_r_exec.png', pos=[0,0], size=[383.7,700])
#  FOOT STIMULI
foot_l_plan = visual.ImageStim(win, image=f'{current_directory}/stimuli/foot_l_plan.png', pos=[0,0], size=[383.7,700])
foot_r_plan = visual.ImageStim(win, image=f'{current_directory}/stimuli/foot_r_plan.png', pos=[0,0], size=[383.7,700])
foot_l_exec = visual.ImageStim(win, image=f'{current_directory}/stimuli/foot_l_exec.png', pos=[0,0], size=[383.7,700])
foot_r_exec = visual.ImageStim(win, image=f'{current_directory}/stimuli/foot_r_exec.png', pos=[0,0], size=[383.7,700])
stimuli_dict = {
    'hand_l_plan': hand_l_plan,'hand_r_plan': hand_r_plan,
    'hand_l_exec': hand_l_exec,'hand_r_exec': hand_r_exec,
    'foot_l_plan': foot_l_plan,'foot_r_plan': foot_r_plan,
    'foot_l_exec': foot_l_exec,'foot_r_exec': foot_r_exec,
}
#  SOUND STIMULI
# correct_sound = sound.Sound(f'{current_directory}/stimuli/zapsplat_multimedia_game_sound_short_beep_earn_point_pick_up_item_001_78373.wav')
# incorrect_sound = sound.Sound(f'{current_directory}/stimuli/zapsplat_multimedia_game_sound_short_high_pitched_buzzer_78377.wav')

#  TEXT STIMULI
instruction_dict = {
    'good': 'Great Job!',
    # Initial Explanation
    0.0 : 'Welcome to the Body Go/No Go Task!\n\nPress space to continue.',
    1.0 : 'In this expiriment, you will identify what side of the body a something is happening on.\n\nPress space to continue.',
    1.1: 'You will only press the button when the figure is green. When the figure is yellow you should not press any button.\n\nPress space to continue.',
    # Hand Placement Instructions
    2.0 : "Please place one finger of your left hand on the 'z' key and press it.",
    3.0 : "Please place one finger of your right hand on the 'm' key and press it.",
    # Explain the task
    4.0 : "On the figure on the screen you you will see one of the hands or feet change color.\n\nPress 'z' or 'm' to continue.",
    4.1 : "Your job is to press the key corresponding to the side of the body that changed color as fast as you can only when the color is green.\n\nPress 'z' or 'm' to continue.",
    4.2 : "If the left hand or foot becomes green, press the 'z' key with your left hand.\n\nPress 'z' or 'm' to continue.",
    4.3 : "If the right hand or foot becomes green, press the 'm' key with your right hand.\n\nPress 'z' or 'm' to continue.",
    4.35 : "If the figure is yellow, do not press any button. After 2 seconds you will progress.\n\nPress 'z' or 'm' to continue.",
    4.4 : "You will only have 2 seconds to respond to green body parts, so answer as fast as you can.\n\nPress 'z' or 'm' to continue.",
    4.5 : "You will get feedback on whether you are correct or not, so you can learn from your mistakes.\n\nPress 'z' or 'm' to continue.",
    4.6 : "If you make a mistake or don't asswer fast enough, you will see a red X and hear this buzzer.\n\nPress 'z' or 'm' to continue.",
    4.7 : "If you answer correctly, you will see a hear this sound and move on to the next trial.\n\nPress 'z' or 'm' to continue.",
    4.8 : "You will have a short break after every 10 trials.\n\nPress 'z' or 'm' to continue.",
    # Prepare to start the task
    5.0 : "You are now ready to start the task.\n\nPress 'z' or 'm' to begin.",
    # Break Instructions
    'break' : 'Take a short break. You will be able to continue after 5 seconds.\n\nPress "z" or "m" when you are ready to continue.',
    # MISC
    'q' : 'You pressed the "q" key. The experiment will now end.',
    'slow' : 'Too Slow!',
    'incorrect' : 'Incorrect!',
    'fast' : 'Too Fast!\n\nPlease wait for the trial to start.',
}

