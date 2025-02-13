from psychopy import visual, event, core
# import os
# from generate_trials import generate_trials
# from helper import get_runtime_vars # import_trials, load_files, get_keyboard_response

"""
This experiment was created for COGS 219 Final Project using PsychoPy (v2024.1.1).
"""

# open a window
win = visual.Window([1000,800], color="lightgray", units='pix', checkTiming=False)

"""# get runtime variables 
order = ['subj_code', 'seed']
runtime_vars = get_runtime_vars({'subj_code':'subj_01', 'seed':10}, order)
print(runtime_vars)

# generate trials
generate_trials(runtime_vars['subj_code'], runtime_vars['seed'])

positions = {'center': (0,0)}
separator=","

# preload
images_directory = load_files(os.path.join(os.getcwd(),"stimuli","images"), '.jpg',fileType="image",win=win)
print(images_dictionary)
"""

# placeholder = visual.Rect(win,width=180,height=80, fillColor="lightgray",lineColor="black", lineWidth=6,pos=[0,0])
instruction = visual.TextStim(win,text="In this experiment, you just need to move your body according to the instructions.\nDuring the experiment, a symbol will be drawn on a specific body part.\nOne of the following four symbols will appear.\n (PIC) \n\n\n PRESS any key to start.",
                              color="black", pos=[0,0]) # height=50

instruction.draw()
win.flip()

# Wait for a key press to proceed
while not event.getKeys():
    pass  # Wait until any key is pressed
                              
instruction = visual.TextStim(win, text="When the instruction begins, you need to move your body part that the symbol is placed on.\n\nIf the symbol is on two parts, you should move both parts at the same time.\n\nWhen the central fixation point appears, you can stop moving and wait for the next instruction.", 
                              color="black",pos=[0,0]) # height=10, 
instruction.draw()
win.flip()

# Wait for a key press to proceed
while not event.getKeys():
    pass  # Wait until any key is pressed

if event.getKeys(['q']):
    win.close()
    core.quit()


"""
# single movement trial (6~11.5s)

     # planning phase (2~6.5s)
        # read in trials
            trial_path = os.path.join(os.getcwd(),'trials',runtime_vars['subj_code']+'_trials.csv')
            trial_list = import_trials(trial_path)
            print(trial_list)

        # open file to write data too and store a header
            data_file = open(os.path.join(os.getcwd(),'data',runtime_vars['subj_code']+'_data.csv'),'w')
            header = separator.join(['subj_code',"seed"])
            data_file.write(header+'\n')
        
        # trial loop
     # execution phase (4~8.5s)
     # fixation phase 

 # dual movement trial (6~11.5s)
     # planning phase (2~6.5s)
     # execution phase (4~8.5s)
     # fixation phase 
"""



