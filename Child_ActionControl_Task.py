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
instruction = visual.TextStim(win,text="In this experiment, you need to move your body according to the instructions.\nDuring the experiment, a symbol will be drawn on a specific body part.\n (PIC) \n\n\n PRESS any key to proceed.",
                              color="black", pos=[0,0]) 

instruction.draw()
win.flip()

# Wait for a key press to proceed
while not event.getKeys():
    pass  # Wait until any key is pressed
                              
instruction = visual.TextStim(win, text="During the experiment, you will see one of these three arrows: \n\n\n (PIC of all 3 arrows)", 
                              color="black",pos=[0,0])  
instruction.draw()
win.flip()
core.wait(5)

# make this into for loop later? 
instruction = visual.TextStim(win, text="When you see this arrow, \n move your body part LEFT and RIGHT \n\n\n (PIC1)", 
                              color="black",pos=[0,0]) 

instruction.draw()
win.flip()
core.wait(5)

instruction = visual.TextStim(win, text="When you see this arrow, \n Rotate your body part CLOCKWISE \n\n\n (PIC2)", 
                              color="black",pos=[0,0]) 

instruction.draw()
win.flip()
core.wait(5)

instruction = visual.TextStim(win, text="When you see this arrow, \n Rotate your body part ANTICLOCKWISE \n\n\n (PIC3)", 
                              color="black",pos=[0,0]) 

instruction.draw()
win.flip()
core.wait(5)

instruction = visual.TextStim(win, text="Let's have a practice run. How would you move your body? \n\n\n (PIC) \n\n\n Press any key to move on after instructor's approval", 
                              color="black",pos=[0,0]) 

instruction.draw()
win.flip()

# Wait for a key press to proceed
while not event.getKeys():
    pass  # Wait until any key is pressed

if event.getKeys(['q']):
    win.close()
    core.quit()


"""
Original adult action control task paradigm: 

# single movement trial (6~11.5s)

     # planning phase (2~6.5s)
     # execution phase (4~8.5s)
     # fixation phase 

 # dual movement trial (6~11.5s)
     # planning phase (2~6.5s)
     # execution phase (4~8.5s)
     # fixation phase 
"""



