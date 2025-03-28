# imports
from psychopy import visual, sound, event, core, gui
import os
from helper import generate_trials, check_paths
import time

"""
This task is meant to establish minimum task competency prior to undertaking the task in the MRI scanner. This expiriment is designed to determine a participant's ability to distinguish stimuli presented in their right and left visual field. 
Stimuli are presented on a body and appear in one of four locations: left hand, right hand, left foot, and right foot.
The body locations will be highlighted in either yellow or green.
Participants will be asked to press the 'z' key if the left side of the body is highlighted and the 'm' key if the right side of the body is highlighted, and they must respond within 2 seconds.
Participants will receive feedback on their responses. Brief pauses will be given after every 10 trials.

This experiment was created partly for UCSD's COGS 219 (WI25) Final Project using PsychoPy (v2024.1.1).

Updated 03/11/2025 by JA 
"""
##### MAKE SURE ALL THE PIECES ARE IN THE RIGHT PLACE #####
current_directory = os.path.dirname(os.path.abspath(__file__))
check_paths(current_directory, task='LeftRight')

##### Get runtime variables with the psychopy GUI#####
def get_runtime_vars(vars_to_get,order,exp_version="experiment_code_for_reference"):
    infoDlg = gui.DlgFromDict(dictionary=vars_to_get, title=exp_version, order=order)
    if infoDlg.OK:
        return vars_to_get
    else: 
        print('User Cancelled')
order =  ['subj_code','seed','num_trials']
runtime_vars = get_runtime_vars({'subj_code':'S001', 'seed':1, 'num_trials':50}, order)
# print(runtime_vars)

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
stimuli_dict = {
    'hand_l_plan': hand_l_plan,'hand_r_plan': hand_r_plan,
    'hand_l_exec': hand_l_exec,'hand_r_exec': hand_r_exec,
    'foot_l_plan': foot_l_plan,'foot_r_plan': foot_r_plan,
    'foot_l_exec': foot_l_exec,'foot_r_exec': foot_r_exec,
}

#  SOUND STIMULI
correct_sound = sound.Sound(f'{current_directory}/stimuli/zapsplat_multimedia_game_sound_short_beep_earn_point_pick_up_item_001_78373.wav')
incorrect_sound = sound.Sound(f'{current_directory}/stimuli/zapsplat_multimedia_game_sound_short_high_pitched_buzzer_78377.wav')
#voice_over = sound.Sound(f'{current_directory}/stimuli/LR_stimuli/Voiceover/leftright_task.m4a') # voiceover by Salma Zreik

#  TEXT STIMULI
instruction_dict = {
    'good': 'Great Job!',
    # Initial Explanation
    0.0 : 'Welcome to the Left Right Task!\n\nPress space to continue.',
    1.0 : 'In this expiriment, you will identify what side of the body a something is happening on.\n\nPress space to continue.',
    # Hand Placement Instructions
    2.0 : "Please place one finger of your left hand on the 'z' key and press it.",
    3.0 : "Please place one finger of your right hand on the 'm' key and press it.",
    # Explain the task
    4.0 : "On the figure on the screen you you will see one of the hands or feet change color.\n\nPress 'z' or 'm' to continue.",
    4.1 : "Your job is to press the key corresponding to the side of the body that changed color as fast as you can.\n\nPress 'z' or 'm' to continue.",
    4.2 : "If the left hand or foot changes color, press the 'z' key with your left hand.\n\nPress 'z' or 'm' to continue.",
    4.3 : "If the right hand or foot changes color, press the 'm' key with your right hand.\n\nPress 'z' or 'm' to continue.",
    4.4 : "You will only have 2 seconds to respond, so answer as fast as you can.\n\nPress 'z' or 'm' to continue.",
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
    'end' : 'End of the experiment. Closing now...'
}

instruction = visual.TextStim(win, text='', color='black', pos=[0,0], height=25)
def instruct(x):
    win.flip()
    core.wait(0.25)
    instruction.setText(instruction_dict[x])
    instruction.draw()
    win.flip()

def display_feedback(feedback,time=1.0):
    instruction.setText(instruction_dict[feedback])
    instruction.setColor('red')
    instruction.draw()
    win.flip()
    core.wait(time)
    instruction.setColor('black')

def present_stimulus(part, plan_or_exec):
    win.flip()
    core.wait(0.25)
    figure.draw()
    stimuli_dict[f'{part}_{plan_or_exec}'].draw()
    timer.reset()
    win.flip()

def get_feedback(key_that_you_pressed, part, reaction_time):
    if key_that_you_pressed:
        # evaulate a key press
        if reaction_time < 200:
            sound_off(incorrect_sound)
            display_feedback('fast',time=4.0)
            output = 0
        elif key_that_you_pressed[0] == 'z':
            if part in ['hand_l', 'foot_l']:
                sound_off(correct_sound)
                output = 1
            else:
                sound_off(incorrect_sound)
                display_feedback('incorrect',time=1.0)
                output = 0
        elif key_that_you_pressed[0] == 'm':
            if part in ['hand_r', 'foot_r']:
                sound_off(correct_sound)
                output = 1
            else:
                sound_off(incorrect_sound)
                display_feedback('incorrect',time=1.0)
                output = 0
    else: # no key press too slow
        sound_off(incorrect_sound)
        display_feedback('slow',time=1.0)
        output = 0
    return(output)

def sound_off(sound):
    sound.play()
    core.wait(float((sound.getDuration())))
    sound.stop()

##### Generate trials #####
generate_trials(runtime_vars['subj_code'], runtime_vars['seed'], runtime_vars['num_trials'], task='LeftRight')

##### Get the trails #####
trials = []
with open(f'{current_directory}/trials/LeftRight_trials/{runtime_vars["subj_code"]}_LeftRight_trials.csv', 'r') as trials_file:
    for line in trials_file:
        if line.startswith('subj_code'):
            continue
        trials.append(line.strip().split(','))

##### Run the task #####

# Initial Explanation
instruct(0.0)
event.waitKeys(keyList=['space'])
instruct(1.0)
event.waitKeys(keyList=['space'])
instruct(2.0)
event.waitKeys(keyList=['z'])
instruct('good')
core.wait(2.0)
instruct(3.0)
event.waitKeys(keyList=['m'])
instruct('good')
core.wait(2.0)
instruct(4.0)
event.waitKeys(keyList=['z','m'])
instruct(4.1)
event.waitKeys(keyList=['z','m'])
instruct(4.2)
event.waitKeys(keyList=['z','m'])
instruct(4.3)
event.waitKeys(keyList=['z','m'])
instruct(4.4)
event.waitKeys(keyList=['z','m'])
instruct(4.5)
event.waitKeys(keyList=['z','m'])
instruct(4.6)
sound_off(incorrect_sound)
event.waitKeys(keyList=['z','m'])
instruct(4.7)
sound_off(correct_sound)
event.waitKeys(keyList=['z','m'])
instruct(4.8)
event.waitKeys(keyList=['z','m'])
instruct(5.0)
event.waitKeys(keyList=['z','m'])

# run the task
trial_num = 1
if not os.path.exists(f'{current_directory}/data/LeftRight_data/{runtime_vars["subj_code"]}_LeftRight_data.csv'):
    results_file = open(f'{current_directory}/data/LeftRight_data/{runtime_vars["subj_code"]}_LeftRight_data.csv', 'w')
    results_file.write('trial_num,subj_code,seed,part,plan_or_exec,correct,reaction_time\n')
else:
    results_file = open(f'{current_directory}/data/LeftRight_data/{runtime_vars["subj_code"]}_LeftRight_data.csv', 'a')
for trial in trials:
    # get the trial variables
    subj_code, seed, part, plan_or_exec = trial
    present_stimulus(part, plan_or_exec)

    key_that_you_pressed = event.waitKeys(keyList=['z','m','q'], maxWait=2.0)
    reaction_times = reaction_times + [round(timer.getTime() * 1000,0)] # get reaction time in MS
    
    fb = get_feedback(key_that_you_pressed, part, reaction_times[-1])
    if (trial_num%10) == 0: # Break every 10 trials
        instruct('break')
        core.wait(5.0)
        event.waitKeys(keyList=['z','m'])

    # emergency Q kill switch
    if key_that_you_pressed and key_that_you_pressed[0] == 'q':
        break 
    
    # record the results
    results_file.write(f'{trial_num},{subj_code},{seed},{part},{plan_or_exec},{fb},{reaction_times[-1]}\n')
    trial_num += 1

# Shut down
results_file.close()
instruct('end')
win.close()
core.quit()
