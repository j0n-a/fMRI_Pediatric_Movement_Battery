# imports
from psychopy import visual, event, core, gui
import os
from helper import generate_trials

"""
This expiriment is designed to determine a participants ability to destinguish stimuli presented in their right and left visual 
field. 

This experiment was created for UCSD's COGS 219 (WI25) Final Project using PsychoPy (v2024.1.1).

Updated 02/20/2025 by JA 
"""

##### MAKE SURE ALL THE PIECES ARE IN THE RIGHT PLACE #####
current_directory = os.path.dirname(os.path.abspath(__file__))
# Check that stimuli are available
if not os.path.exists(f'{current_directory}/stimuli/figure.png'):
    if not os.path.exists(f'{current_directory}/stimuli'): # Does the folder exist?
        raise FileNotFoundError(f'Stimuli folder not found in {current_directory}.\nPlease ensure that the stimuli folder is in the same directory as this script.')
    else: # Does the figure exist?
        raise FileNotFoundError(f'Figure not found in {current_directory}/stimuli.\nPlease ensure that the stimuli folder contains the required .png files distributed with these programs.')
# Check that there is a trials folder and if not make it
if not os.path.exists(f'{current_directory}/trials'):
    print(f'Trials folder not found in {current_directory}. Creating trials folder here:\n\t{current_directory}/trials.')
    os.makedirs(f'{current_directory}/trials')
    if not os.path.exists(f'{current_directory}/trials/LeftRight_trials'):
        print(f'LeftRight_trials folder not found in {current_directory}/trials. Creating LeftRight_trials folder here:\n\t{current_directory}/trials/LeftRight_trials.')
        os.makedirs(f'{current_directory}/trials/LeftRight_trials')
# Check that there is a data folder and if not we make it
if not os.path.exists(f'{current_directory}/data'):
    print(f'Data folder not found in {current_directory}. Creating data folder here:\n\t{current_directory}/data.')
    os.makedirs(f'{current_directory}/data')

##### Get runtime variables with the psychopy GUI#####
def get_runtime_vars(vars_to_get,order,exp_version="experiment_code_for_reference"):
    infoDlg = gui.DlgFromDict(dictionary=vars_to_get, title=exp_version, order=order)
    if infoDlg.OK:
        return vars_to_get
    else: 
        print('User Cancelled')
order =  ['subj_code','seed','num_trials']
runtime_vars = get_runtime_vars({'subj_code':'S001', 'seed':1, 'num_trials':48}, order)
# print(runtime_vars)

##### Set up psychopy features for the task #####
# set window paramaters
win = visual.Window([1000,800], color='lightgray', units='pix', checkTiming=False)
# preopen all the important stimuli
#  FIGURE STIMULI
figure = visual.ImageStim(win, image=f'{current_directory}/stimuli/figure.png', pos=[0,0])
#  HAND STIMULI
hand_l_plan = visual.ImageStim(win, image=f'{current_directory}/stimuli/hand_l_plan.png', pos=[0,0])
hand_r_plan = visual.ImageStim(win, image=f'{current_directory}/stimuli/hand_r_plan.png', pos=[0,0])
hand_l_exec = visual.ImageStim(win, image=f'{current_directory}/stimuli/hand_l_exec.png', pos=[0,0])
hand_r_exec = visual.ImageStim(win, image=f'{current_directory}/stimuli/hand_r_exec.png', pos=[0,0])
#  FOOT STIMULI
foot_l_plan = visual.ImageStim(win, image=f'{current_directory}/stimuli/foot_l_plan.png', pos=[0,0])
foot_r_plan = visual.ImageStim(win, image=f'{current_directory}/stimuli/foot_r_plan.png', pos=[0,0])
foot_l_exec = visual.ImageStim(win, image=f'{current_directory}/stimuli/foot_l_exec.png', pos=[0,0])
foot_r_exec = visual.ImageStim(win, image=f'{current_directory}/stimuli/foot_r_exec.png', pos=[0,0])
#  TEXT STIMULI
instruction_dict = {
    # Initial Explanation
    1.0 : 'In this expiriment, you will identify what side of the body a something is happening on.',
    # Hand Placement Instructions
    2.0 : "Please place one finger of your left hand on the 'z' key and press it.",
    2.1 : 'Great job!',
    2.2 : "That's not quite right. Place one finger of your left hand on the 'z' key and press it.",
    3.0 : "Please place one finger of your right hand on the 'm' key and press it.",
    3.1 : 'Great job!',
    3.2 : "That's not quite right. Place one finger of your right hand on the 'm' key and press it.",
    # Explain the task
    4.0 : 'On the figure on the screen you you will see one of the hands or feet change color.',
    4.1 : 'Your job is to press the key corresponding to the side of the body that changed color as fast as you can.',
    4.2 : "If the left hand or foot changes color, press the 'z' key with your left hand.",
    4.3 : "If the right hand or foot changes color, press the 'm' key with your right hand.",
    4.4 : 'You will only have 2 seconds to respond, so answer as fast as you can.',
    4.5 : 'You will get feedback on whether you are correct or not, so you can learn from your mistakes.',
    4.6 : "If you make a mistake or don't asswer fast enough, you will see a red X and hear this buzzer.",
    4.7 : "If you answer correctly, you will see a hear this sound and move on to the next trial.",

    

}
instruction = visual.TextStim(win, text='', color='black', pos=[0,0])

##### Generate trials #####
generate_trials(runtime_vars['subj_code'], runtime_vars['seed'], runtime_vars['num_trials'], task='LeftRight')

##### Get the trails #####
trials = []
with open(f'{current_directory}/trials/{runtime_vars["subj_code"]}_LeftRight_trials.csv', 'r') as trials_file:
    for line in trials_file:
        if line.startswith('subj_code'):
            continue
        trials.append(line.strip().split(','))


# # placeholder = visual.Rect(win,width=180,height=80, fillColor="lightgray",lineColor="black", lineWidth=6,pos=[0,0])
# instruction = visual.TextStim(win,text="In this experiment, you need to move your body according to the instructions.\nDuring the experiment, a symbol will be drawn on a specific body part.\n (PIC) \n\n\n PRESS any key to proceed.",
#                               color="black", pos=[0,0]) 

# instruction.draw()
# win.flip()

# # Wait for a key press to proceed
# while not event.getKeys():
#     pass  # Wait until any key is pressed
                              
# instruction = visual.TextStim(win, text="During the experiment, you will see one of these three arrows: \n\n\n (PIC of all 3 arrows)", 
#                               color="black",pos=[0,0])  
# instruction.draw()
# win.flip()
# core.wait(5)

# # make this into for loop later? 
# instruction = visual.TextStim(win, text="When you see this arrow, \n move your body part LEFT and RIGHT \n\n\n (PIC1)", 
#                               color="black",pos=[0,0]) 

# instruction.draw()
# win.flip()
# core.wait(5)

# instruction = visual.TextStim(win, text="When you see this arrow, \n Rotate your body part CLOCKWISE \n\n\n (PIC2)", 
#                               color="black",pos=[0,0]) 

# instruction.draw()
# win.flip()
# core.wait(5)

# instruction = visual.TextStim(win, text="When you see this arrow, \n Rotate your body part ANTICLOCKWISE \n\n\n (PIC3)", 
#                               color="black",pos=[0,0]) 

# instruction.draw()
# win.flip()
# core.wait(5)

# instruction = visual.TextStim(win, text="Let's have a practice run. How would you move your body? \n\n\n (PIC) \n\n\n Press any key to move on after instructor's approval", 
#                               color="black",pos=[0,0]) 

# instruction.draw()
# win.flip()

# # Wait for a key press to proceed
# while not event.getKeys():
#     pass  # Wait until any key is pressed

# if event.getKeys(['q']):
#     win.close()
#     core.quit()


# """
# Original adult action control task paradigm: 

# # single movement trial (6~11.5s)

#      # planning phase (2~6.5s)
#      # execution phase (4~8.5s)
#      # fixation phase 

#  # dual movement trial (6~11.5s)
#      # planning phase (2~6.5s)
#      # execution phase (4~8.5s)
#      # fixation phase 
# """



