from psychopy import visual, sound, event, core, gui
import os
from helper import generate_trials, check_paths

'''
This experiment was created for COGS 219 Final Project using PsychoPy (v2024.1.1).

Start with the right path!!

### Note ###
1. reaction time recording at the end of the plan phase, too slow feedback = 10s 
2. planning (~10s) -> execute (~10s), instructor give feedback and press the key (c for correct, i for incorrect)

### To-do ###
- add sound? 
- fixation after execution?
- change path in the end

last updated 03/05, SP
'''

##### MAKE SURE ALL THE PIECES ARE IN THE RIGHT PLACE #####
current_directory = os.path.dirname(os.path.abspath(__file__))
check_paths(current_directory, task='ActionControl')

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

timer = core.Clock()
reaction_times = []

win = visual.Window([1000,800], color="black", units='pix', checkTiming=False)

# preload all the important stimuli
# FIGURE STIMULI
figure = visual.ImageStim(win, image=f'{current_directory}/stimuli/AC_stimuli/AC_figure.png', pos=[0,0], size=[500,700])

# Define all stimuli filenames
stimuli_filenames = [
    "AC_foot_l_exec_clockwise.png", "AC_foot_l_exec_counterclockwise.png", "AC_foot_l_exec_leftright.png",
    "AC_foot_l_plan_clockwise.png", "AC_foot_l_plan_counterclockwise.png", "AC_foot_l_plan_leftright.png",
    "AC_foot_r_exec_clockwise.png", "AC_foot_r_exec_counterclockwise.png", "AC_foot_r_exec_leftright.png",
    "AC_foot_r_plan_clockwise.png", "AC_foot_r_plan_counterclockwise.png", "AC_foot_r_plan_leftright.png",
    "AC_hand_l_exec_clockwise.png", "AC_hand_l_exec_counterclockwise.png", "AC_hand_l_exec_leftright.png",
    "AC_hand_l_plan_clockwise.png", "AC_hand_l_plan_counterclockwise.png", "AC_hand_l_plan_leftright.png",
    "AC_hand_r_exec_clockwise.png", "AC_hand_r_exec_counterclockwise.png", "AC_hand_r_exec_leftright.png",
    "AC_hand_r_plan_clockwise.png", "AC_hand_r_plan_counterclockwise.png", "AC_hand_r_plan_leftright.png"
]

# Initialize stimuli dictionary
stimuli_dict = {}
# Create stimuli dynamically
for filename in stimuli_filenames:
    key = filename.replace(".png", "").replace("AC_", "")  # Remove file extension for dictionary keys
    stimuli_dict[key] = visual.ImageStim(win, image=os.path.join(current_directory, "stimuli", "AC_stimuli", filename), pos=[0, 0], size=[500, 700])

#  TEXT STIMULI
instruction_dict = {
    'good': 'Great Job!',
    # Initial Explanation
    0.0 : 'Welcome to the Action Control Task! \n\n From now on, press SPACE to progress.',
    1.0 : 'In this experiment, your job is to plan and execute certain body movements according to the instructions. \n\n',
    # Arrows
    2.0 : 'During the experiment, you will see one of three arrows on the body figure. \n\n',
    2.1 : '1) When you see this arrow, move your body part LEFT and RIGHT',
    2.2 : '2) When you see this arrow, Rotate your body part CLOCKWISE',
    2.3 : '3) When you see this arrow, Rotate your body part COUNTER-CLOCKWISE',
    # Rules
    3.0 : "On the body figure on the screen, you will see one of the hands or feet in colors.\n\n",
    3.1 : "If hand or foot is in yellow, PLAN your movement in 10 seconds. \n\n **YELLOW = PLANNING** \n\n Remember: Press SPACE when you're done with planning and ready to execute. \n Execution phase will automatically start after 10 seconds.",
    3.2 : "When the color of the arrows changes into green, EXECUTE your movement in 10 seconds. \n\n **GREEN = EXECUTION** \n\n After execution, you will get feedback from the instructor on whether you are correct or not \n\n",
    3.3 : "If you answer correctly, you will see 'correct' sign with this sound and move on to the next trial.",
    3.4 : "If you make a mistake or don't respond fast enough with execution, \n you will see 'incorrect' sign and hear this buzzer.",
    3.5 : "You will have a short break after every 10 trials.\n\n",
    # Prepare to start the task
    4.0 : 'You are now ready to start the task! \n\n Press SPACE to start the experiment.',
    # Break Instructions
    'break' : 'Take a short break. You will be able to continue after 5 seconds.\n\n Press SPACE when you are ready to continue.',
    # MISC
    'q' : 'You pressed the "q" key. The experiment will now end.',
    'slow' : 'Too Slow!\n\nPlease try to execute faster.',
    'fast' : 'Too Fast!\n\nPlease wait for the trial to start.',
    'correct' : 'Correct!',
    'incorrect' : 'Incorrect!',
    'plan_done' : "Press SPACE when you're done with planning and ready to execute."
}

image_dict = {
    2.1: os.path.join(current_directory, "stimuli", "AC_stimuli", "AC_left_right_yellow.png"),
    2.2: os.path.join(current_directory, "stimuli", "AC_stimuli", "AC_clockwise_yellow.png"),
    2.3: os.path.join(current_directory, "stimuli", "AC_stimuli", "AC_counterclockwise_yellow.png")
}

#  SOUND STIMULI
correct_sound = sound.Sound(f'{current_directory}/stimuli/zapsplat_multimedia_game_sound_short_beep_earn_point_pick_up_item_001_78373.wav')
incorrect_sound = sound.Sound(f'{current_directory}/stimuli/zapsplat_multimedia_game_sound_short_high_pitched_buzzer_78377.wav')

instruction_stim = visual.TextStim(win, text='', color='white', pos=[0,0], wrapWidth=1000)

def instruct(x):
    win.flip()
    core.wait(0.25)
    instruction_stim.setText(instruction_dict[x])
    instruction_stim.draw()

    if x in image_dict:
        image_stim = visual.ImageStim(win, image=image_dict[x], pos=[0, -100], size=(200, 200))
        image_stim.draw()

    win.flip()

    # Play sounds for specific instructions
    if x == 3.3:
        sound_off(correct_sound)
    elif x == 3.4:
        sound_off(incorrect_sound)
    
    event.waitKeys(keyList=['space'])

def display_feedback(feedback,time=1.0):
    incorrect_sound.play()
    instruction_stim.setText(instruction_dict[feedback])
    instruction_stim.setColor('white')
    instruction_stim.setPos((0, 0)) 
    instruction_stim.draw()
    win.flip()
    core.wait(time)
    # instruction_stim.setColor('white')

def present_stimulus(part, plan_or_exec, movement): 
    win.flip()
    core.wait(0.25)
    figure.draw()
    stimuli_dict[f'{part}_{plan_or_exec}_{movement}'].draw()
    if plan_or_exec == 'plan':
        instruction_stim.setText(instruction_dict['plan_done'])
        instruction_stim.setColor('white')
        instruction_stim.setPos((0, -350))  # Adjust as needed 
        instruction_stim.draw()
    win.flip()  # Ensure it appears BEFORE moving on
    timer.reset()

def get_feedback(key_that_you_pressed, reaction_time):
    if key_that_you_pressed:
        # evaulate a key press
        if reaction_time < 1000:
            display_feedback('fast',time=4.0)
            instruction_stim.setColor('white')
            output = 'fast'
        if key_that_you_pressed[0] == 'c':
            sound_off(correct_sound)
            display_feedback('correct',time=1.0)
            output = 1
        elif key_that_you_pressed[0] == 'i':
            # if part in ['hand_r', 'foot_r']:
            sound_off(incorrect_sound)
            display_feedback('incorrect',time=1.0)
            output = 0
        elif key_that_you_pressed[0] == 'space':
            if plan_or_exec == 'plan':
                output = ""
            else: 
                output = reaction_time
    else:  # No key press (too slow)
        if plan_or_exec == 'plan':  
            output = ""
        else:
            sound_off(incorrect_sound)
            display_feedback('slow', time=1.0)
            output = "slow"
    return(output)

def sound_off(sound):
    sound.play()
    core.wait(float((sound.getDuration())))
    sound.stop()

##### Generate trials #####
generate_trials(runtime_vars['subj_code'], runtime_vars['seed'], runtime_vars['num_trials'], task='ActionControl')

##### Get the trials #####
trials = []
with open(f'{current_directory}/trials/ActionControl_trials/{runtime_vars["subj_code"]}_ActionControl_trials.csv', 'r') as trials_file:
    for line in trials_file:
        if line.startswith('subj_code'):
            continue
        trials.append(line.strip().split(','))

##### Run the task #####

# Filter out only the numeric (float) keys and sort them
numeric_keys = [key for key in instruction_dict.keys() if isinstance(key, float)]
sorted_numeric_keys = sorted(numeric_keys)

# Iterate over the sorted numeric keys 
sorted_numeric_keys = sorted([key for key in instruction_dict if isinstance(key, float)])
for key in sorted_numeric_keys:
    print(key)
    instruct(key)

# Run the task
trial_num = 1
if not os.path.exists(f'{current_directory}/data/ActionControl_data/{runtime_vars["subj_code"]}_ActionControl_data.csv'):
    results_file = open(f'{current_directory}/data/ActionControl_data/{runtime_vars["subj_code"]}_ActionControl_data.csv', 'w')
    results_file.write('trial_num,subj_code,seed,part,plan_or_exec,movement,correct,reaction_time\n')
else:
    results_file = open(f'{current_directory}/data/ActionControl_data/{runtime_vars["subj_code"]}_ActionControl_data.csv', 'a')
for trial in trials:
    # get the trial variables

    ############ ********************************************************************************** ############
    ############ SUJIN I ADDED IN TEMPORAL JITTER TO THE TRIAL FILE SO IT MATCHES GORDON ET AL 2023 ############
    ############ ********************************************************************************** ############
    subj_code, seed, part, plan_or_exec, movement, temporal_jitter = trial
    present_stimulus(part, plan_or_exec, movement)

    key_that_you_pressed = event.waitKeys(
        keyList=['q','space'] if plan_or_exec == 'plan' else ['c','i','q'], maxWait=10.0)
    
    reaction_times = reaction_times + [round(timer.getTime() * 1000,0)] # get reaction time in MS
    print(reaction_times[-1])
    
    fb = get_feedback(key_that_you_pressed, reaction_times[-1]) # 
    if (trial_num%10) == 0: # Break every 10 trials
        instruct('break')
        core.wait(5.0)
        event.waitKeys(keyList=['space'])

    # emergency Q kill switch
    if key_that_you_pressed and key_that_you_pressed[0] == 'q':
        break 
    
    # record the results
    results_file.write(f'{trial_num},{subj_code},{seed},{part},{plan_or_exec},{movement},{fb},{reaction_times[-1]}\n') 
    trial_num += 1

# Shut down
results_file.close()
win.close()
core.quit()
