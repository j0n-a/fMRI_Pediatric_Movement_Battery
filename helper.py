def generate_trials(subj_code, seed, num_trials=48, task=None):
    '''
    Code adapted from work by Dr. Martin Zettersten. Last updated by JA 02-20-2025
    Writes a file named {subj_code}_{task}_trials.csv, one line per trial. Creates a trials subdirectory if one does not exist
    subj_code: a string corresponding to a participant's unique subject code
    seed: an integer specifying the random seed
    num_repetitions: integer specifying total times that combinations of trial type (congruent vs. incongruent) and orientation (upright vs. upside_down) should repeat (total number of trials = 4 * num_repetitions)
    
    Note
    - edited ActionControl
    - edited output folder path
    
    last updated 03/02, SP.
    '''
    import os
    import random
    import warnings

    # break if you are not given a task
    if task is None:
        raise ValueError('ERROR: You must specify a task')
    elif task not in ['LeftRight', 'GoNoGO', 'ActionControl']:
        raise ValueError('ERROR: You must specify a valid task\nValid tasks are: "LeftRight", "GoNoGO", "ActionControl"')

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
        os.mkdir(f'trials/{task}_trials')
    except FileExistsError:
        # directory already exists
        pass
    trial_file=open(f"trials/{task}_trials/{subj_code}_{task}_trials.csv","w")

    #write header
    separator = ','
    
    # make and write trials 
    trials = []
    if task == 'LeftRight':
        if num_trials < len(parts)*len(plan_or_exec):
            warnings.warn(f'WARNING: You have fewer trials than the number of possible permutations ({len(parts)*len(plan_or_exec)} trial types). Some permutations will not be used.')
        header = separator.join(['subj_code','seed','part','plan_or_exec'])
        trial_file.write(header+'\n')
        for i in range(num_trials):
            pick_part = i%len(parts)
            pick_plan_or_exec = (i//len(parts))%len(plan_or_exec)
            trials.append([subj_code, seed, parts[pick_part], plan_or_exec[pick_plan_or_exec]])
        random.shuffle(trials) # shuffle the trials
        for trial in trials:
            trial_file.write(separator.join([str(x) for x in trial])+'\n')
    elif task == 'GoNoGO':
        if num_trials < len(parts)*len(movements):
            warnings.warn(f'WARNING: You have fewer trials than the number of possible permutations ({len(parts)*len(movements)} trial types). Some permutations will not be used.')
        header = separator.join(['subj_code','seed','part','plan_or_exec'])
        trial_file.write(header+'\n')
        for i in range(num_trials): 
            pick_part = i%len(parts)
            percentile_die = random.randint(1,100) 
            if percentile_die <= 70: # ~70% of the time we want to plan
                plan_or_exec = 'exec'
            else:
                plan_or_exec = 'plan'
            trials.append([subj_code, seed, parts[pick_part],plan_or_exec]) # keep plan and exec together in the right order
            random.shuffle(trials) # shuffle the trials
        for trial in trials:
            trial_file.write(separator.join([str(x) for x in trial]) + '\n')
    elif task == 'ActionControl':
        if num_trials < len(parts)*len(movements):
            warnings.warn(f'WARNING: You have fewer trials than the number of possible permutations ({len(parts)*len(movements)} trial types). Some permutations will not be used.')
        header = separator.join(['subj_code','seed','part','movement','plan_temporal_jitter','exec_temporal_jitter'])
        trial_file.write(header+'\n')
        for i in range(num_trials): 
            pick_part = i%len(parts) # iterate through the parts
            pick_movement = (i//len(parts))%len(movements) # for each part, iterate through the movements
            plan_temporal_jitter = random.randint(20, 65)/10 # random temporal jitter for the plan - range form Gordon et al. 2023
            exec_temporal_jitter = random.randint(40, 85)/10 
            trials.append([subj_code, seed, parts[pick_part], movements[pick_movement], plan_temporal_jitter, exec_temporal_jitter]) # keep plan and exec together in the right order
            random.shuffle(trials) # shuffle the trials
        for trial in trials:
            trial_file.write(separator.join([str(x) for x in trial]) + '\n')
    else:
        raise ValueError('ERROR: You must specify a valid task\nValid tasks are: "LeftRight", "GoNoGO", "ActionControl"')

    #close the file
    trial_file.close()

def check_paths(current_directory, task=None):
    '''
    Check that the paths for the stimuli and the trials exist
    '''
    import os

    # check that current_directory exists, is a string, and is a directory
    if not isinstance(current_directory,str):
        raise ValueError('ERROR: current_directory must be a string.')
    elif not os.path.isdir(current_directory):
        raise FileNotFoundError('ERROR: current_directory must be a string that points to a directory.')
    
    # break if you are not given a task
    if task is None:
        raise ValueError('ERROR: You must specify a task')
    elif task not in ['LeftRight', 'GoNoGO', 'ActionControl']:
        raise ValueError('ERROR: You must specify a valid task\nValid tasks are: "LeftRight", "GoNoGO", "ActionControl"')

    # instanciate task abreviations
    task_abreviations = {
        'LeftRight':'LR', 'GoNoGO':'LR', # LeftRight and GoNoGO have the same stimuli
        'ActionControl':'AC'}

    ##### MAKE SURE ALL THE PIECES ARE IN THE RIGHT PLACE #####
    # Check that stimuli are available
    if not os.path.exists(f'{current_directory}/stimuli/{task_abreviations[task]}_stimuli/{task_abreviations[task]}_figure.png'):
        if not os.path.exists(f'{current_directory}/stimuli'): # Does the folder exist?
            raise FileNotFoundError(f'ERROR: Stimuli folder not found in {current_directory}.\nPlease ensure that the stimuli folder is in the same directory as this script.')
        else: # Does the figure exist?
            raise FileNotFoundError(f'ERROR: Figure not found in {current_directory}/stimuli.\nPlease ensure that the stimuli folder contains the required .png files distributed with these programs.')
    # Check that there is a trials folder and if not make it
    if not os.path.exists(f'{current_directory}/trials/{task}_trials'):
        if not os.path.exists(f'{current_directory}/trials'):
            print(f'Trials folder not found in {current_directory}. Creating trials folder here:\n\t{current_directory}/trials.')
            os.makedirs(f'{current_directory}/trials')
        print(f'{task}_trials folder not found in {current_directory}/trials. Creating {task}_trials folder here:\n\t{current_directory}/trials/{task}_trials.')
        os.makedirs(f'{current_directory}/trials/{task}_trials')
    # Check that there is a data folder and if not we make it
    if not os.path.exists(f'{current_directory}/data/{task}_data'):
        if not os.path.exists(f'{current_directory}/data'):
            print(f'Data folder not found in {current_directory}. Creating data folder here:\n\t{current_directory}/data.')
            os.makedirs(f'{current_directory}/data')
        print(f'{task}_trials folder not found in {current_directory}/trials. Creating {task}_data folder here:\n\t{current_directory}/data/{task}_data.')
        os.makedirs(f'{current_directory}/data/{task}_data')
