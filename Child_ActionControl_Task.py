from psychopy import visual, event, core, gui
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
- check output file
- create illustration, instead of hand/feet, change it to arrow symbols (name them like: foot_l_plan_counterclockwise.png)
- copy yellow arrows in stimuli folder

last updated 03/02, SP
'''

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

timer = core.Clock()
reaction_times = []

win = visual.Window([1000,800], color="lightgray", units='pix', checkTiming=False)

# preload all the important stimuli
# FIGURE STIMULI
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

#  TEXT STIMULI
instruction_dict = {
    'good': 'Great Job!',
    # Initial Explanation
    0.0 : 'Welcome to the Action Control Task! \n\n From now on, press SPACE to progress.',
    1.0 : 'In this experiment, your job is to plan and execute certain body movements according to the instructions. \n\n',
    # Arrows
    2.0 : 'During the experiment, you will see one of three arrows on the body figure. \n\n',
    2.1 : '1) When you see this arrow, \n move your body part LEFT and RIGHT',
    2.2 : '2) When you see this arrow, \n Rotate your body part CLOCKWISE',
    2.3 : '3) When you see this arrow, \n Rotate your body part COUNTER-CLOCKWISE',
    # Rules
    3.0 : "On the body figure on the screen, you will see one of the hands or feet in colors.\n\n",
    3.1 : "If hand or foot is in yellow, PLAN your movement in 10 seconds. \n\n **YELLOW = PLANNING** \n\n Remember: Press SPACE when you're done with planning and ready to execute.",
    3.2 : "When the color of the arrows changes into green, EXECUTE your movement in 10 seconds. \n\n **GREEN = EXECUTION** \n\n After execution, you will get feedback from the instructor on whether you are correct or not \n\n",
    3.3 : "You will have a short break after every 10 trials.\n\n",
    # Prepare to start the task
    4.0 : 'You are now ready to start the task! \n\n Press SPACE to start the experiment.',
    # Break Instructions
    'break' : 'Take a short break. You will be able to continue after 5 seconds.\n\n Press SPACE when you are ready to continue.',
    # MISC
    'q' : 'You pressed the "q" key. The experiment will now end.',
    'slow' : 'Too Slow!',
    'incorrect' : 'Incorrect!',
    'fast' : 'Too Fast!\n\nPlease wait for the trial to start.',
}

image_dict = {
    2.1: os.path.join(current_directory, "stimuli", "left_right_yellow.png"),
    2.2: os.path.join(current_directory, "stimuli", "clockwise_yellow.png"),
    2.3: os.path.join(current_directory, "stimuli", "counterclockwise_yellow.png")
}

instruction_stim = visual.TextStim(win, text='', color='black', pos=[0,0], wrapWidth=1000)

def instruct(x):
    win.flip()
    core.wait(0.25)
    instruction_stim.setText(instruction_dict[x])
    instruction_stim.draw()

    if x in image_dict:
        image_stim = visual.ImageStim(win, image=image_dict[x], pos=[0, -100], size=(80, 80))
        image_stim.draw()

    win.flip()
    event.waitKeys(keyList=['space'])

def display_feedback(feedback,time=1.0):
    # incorrect_sound.play()
    instruction_stim.setText(instruction_dict[feedback])
    instruction_stim.setColor('red')
    instruction_stim.draw()
    win.flip()
    core.wait(time)
    instruction_stim.setColor('black')

def present_stimulus(part, plan_or_exec, movement): # add movement here 
    win.flip()
    core.wait(0.25)
    figure.draw()
    stimuli_dict[f'{part}_{plan_or_exec}_{movement}'].draw()
    timer.reset()
    win.flip()

def get_feedback(key_that_you_pressed, part, reaction_time):
    if key_that_you_pressed:
        # evaulate a key press
        # if reaction_time < 1000:
        #     display_feedback('fast',time=4.0)
        #     instruction.setColor('black')
        #     output = 0
        if key_that_you_pressed[0] == 'c':
            # if part in ['hand_l', 'foot_l']:
                # correct_sound.play()
            display_feedback('correct',time=1.0)
            output = 1
        elif key_that_you_pressed[0] == 'i':
            # if part in ['hand_r', 'foot_r']:
                # correct_sound.play()
                # incorrect_sound.play()
            display_feedback('incorrect',time=1.0)
            output = 0
        elif key_that_you_pressed[0] == 'space':
            output = reaction_time
    else: # no key press too slow
        display_feedback('slow',time=1.0)
        output = 0
    return(output)

##### Generate trials #####
generate_trials(runtime_vars['subj_code'], runtime_vars['seed'], runtime_vars['num_trials'], task='ActionControl')

##### Get the trials #####
trials = []
with open(f'{current_directory}/trials/ActionControl/{runtime_vars["subj_code"]}_ActionControl_trials.csv', 'r') as trials_file:
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
    instruct(key)

# Run the task
trial_num = 1
results_file = open(f'{current_directory}/data/{runtime_vars["subj_code"]}_ActionControl_data.csv', 'w')
results_file.write('trial_num,subj_code,seed,part,plan_or_exec,movement,correct,reaction_time\n')
for trial in trials:
    # get the trial variables
    subj_code, seed, part, plan_or_exec, movement = trial
    present_stimulus(part, plan_or_exec, movement)

    key_that_you_pressed = event.waitKeys(keyList=['c','i','m','q'], maxWait=10.0)
    reaction_times = reaction_times + [round(timer.getTime() * 1000,0)] # get reaction time in MS
    print(reaction_times[-1])
    
    fb = get_feedback(key_that_you_pressed, part, reaction_times[-1]) # 
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
