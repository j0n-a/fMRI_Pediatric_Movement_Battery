def generate_trials(subj_code, seed, num_trials=48, task=None):
    '''
    Code adapted from work by Dr. Martin Zettersten. Last updated by JA 02-20-2025
    Writes a file named {subj_code}_{task}_trials.csv, one line per trial. Creates a trials subdirectory if one does not exist
    subj_code: a string corresponding to a participant's unique subject code
    seed: an integer specifying the random seed
    num_repetitions: integer specifying total times that combinations of trial type (congruent vs. incongruent) and orientation (upright vs. upside_down) should repeat (total number of trials = 4 * num_repetitions)
    '''
    import os
    import random

    # break if you are not given a task
    if task is None:
        raise ValueError('ERROR: You must specify a task')

    # define general parameters and functions here
    random.seed(seed)
    # trial states
    parts = ['hand_l', 'foot_l', 'hand_r', 'foot_r']
    plan_or_exec = ['plan', 'exec']
    movements = ['clockwise', 'counterclockwise','left_right','open_close']
    random.shuffle(parts) # we must shuffle the trials for taks that are not cleanly divisable by the number of permutations
    random.shuffle(plan_or_exec)
    random.shuffle(movements)

    # create a trials folder if it doesn't already exist
    try:
        os.mkdir('trials')
    except FileExistsError:
        trial_file=open(f"trials/{subj_code}_trials.csv","w")

    #write header
    separator = ','
    header = separator.join(['subj_code','seed','part','plan_or_exec'])
    trial_file.write(header+'\n')
    
    # make and write trials 
    trials = []
    for i in range(num_trials):
        pick_part = i%len(parts)
        pick_plan_or_exec = (i//len(parts))%len(plan_or_exec)
        trials.append([subj_code, seed, parts[pick_part], plan_or_exec[pick_plan_or_exec]])
    random.shuffle(trials) # shuffle the trials
    for trial in trials:
        trial_file.write(separator.join([str(x) for x in trial])+'\n')

    #close the file
    trial_file.close()