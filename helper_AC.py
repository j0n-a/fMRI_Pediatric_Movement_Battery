def generate_trials(subj_code, seed, num_trials=48, task=None):
    '''
    Code adapted from work by Dr. Martin Zettersten. Last updated by JA 02-20-2025
    Writes a file named {subj_code}_{task}_trials.csv, one line per trial. Creates a trials subdirectory if one does not exist
    subj_code: a string corresponding to a participant's unique subject code
    seed: an integer specifying the random seed
    num_repetitions: integer specifying total times that combinations of trial type (congruent vs. incongruent) and orientation (upright vs. upside_down) should repeat (total number of trials = 4 * num_repetitions)
    
    last updated 03/04, SP.
    '''
    import os
    import random

    # break if you are not given a task
    if task is None:
        raise ValueError('ERROR: You must specify a task')
    elif task not in ['ActionControl']:
        raise ValueError('ERROR: You must specify a valid task\nValid tasks')

    # define general parameters and functions here
    random.seed(seed)
    # trial states
    parts = ['hand_l', 'foot_l', 'hand_r', 'foot_r']
    plan_or_exec = ['plan', 'exec']
    movements = ['clockwise', 'counterclockwise','leftright'] # 'open_close'
    random.shuffle(parts) # we must shuffle the trials for taks that are not cleanly divisable by the number of permutations
    random.shuffle(plan_or_exec)
    random.shuffle(movements)

    # create a trials folder if it doesn't already exist
    try:
        os.mkdir(f'trials/{task}')
    except FileExistsError:
        # directory already exists
        pass
    trial_file=open(f"trials/{task}/{subj_code}_{task}_trials.csv","w")

    #write header
    separator = ','
    
    # make and write trials 
    trials = []
    if task == 'ActionControl':
        header = separator.join(['subj_code','seed','part','plan_or_exec','movement'])
        trial_file.write(header+'\n')
        for i in range(num_trials // 2): # two trials (plan & execution) per iteration
            pick_part = random.choice(parts)
            pick_movement = random.choice(movements)
            trials.append([subj_code,seed,pick_part,'plan',pick_movement])
            trials.append([subj_code,seed,pick_part,'execute',pick_movement])
        # random.shuffle(trials)
        for trial in trials:
            trial_file.write(separator.join([str(x) for x in trial]) + '\n')
    else:
        raise ValueError('ERROR: You must specify a valid task\nValid tasks')

    #close the file
    trial_file.close()

def check_paths(current_directory):
    '''
    Check that the paths for the stimuli and the trials exist
    '''
    import os

    #check that current_directory exists, is a string, and is a directory
    if not isinstance(current_directory,str):
        raise ValueError('ERROR: current_directory must be a string.')
    elif not os.path.isdir(current_directory):
        raise FileNotFoundError('ERROR: current_directory must be a string that points to a directory.')
    
    ##### MAKE SURE ALL THE PIECES ARE IN THE RIGHT PLACE #####
    # Check that stimuli are available
    if not os.path.exists(f'{current_directory}/stimuli/AC_stimuli/AC_figure.png'):
        if not os.path.exists(f'{current_directory}/stimuli/AC_stimuli'): # Does the folder exist?
            raise FileNotFoundError(f'ERROR: Stimuli folder not found in {current_directory}/stimuli/AC_stimuli.\nPlease ensure that the stimuli folder is in the same directory as this script.')
        else: # Does the figure exist?
            raise FileNotFoundError(f'ERROR: Figure not found in {current_directory}/stimuli/AC_stimuli.\nPlease ensure that the stimuli folder contains the required .png files distributed with these programs.')
    # Check that there is a trials folder and if not make it
    if not os.path.exists(f'{current_directory}/trials/ActionControl'):
        print(f'Trial folder not found in {current_directory}/trials/ActionControl. Creating trials folder here:\n\t{current_directory}/trials/ActionControl.')
        os.makedirs(f'{current_directory}/trials/ActionControl')
    # Check that there is a data folder and if not we make it
    if not os.path.exists(f'{current_directory}/data/ActionControl'):
        print(f'Data folder not found in {current_directory}/data/ActionControl. Creating data folder here:\n\t{current_directory}/data/ActionControl.')
        os.makedirs(f'{current_directory}/data/ActionControl')