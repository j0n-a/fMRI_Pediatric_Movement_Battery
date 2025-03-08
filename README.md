# fMRI-Movement-Battery

These tasks was created by [Sujin Park](https://scholar.google.com/citations?hl=en&user=qS3zgSgAAAAJ) (sup031@ucsd.edu) and [Jonathan Ahern](https://scholar.google.com/citations?user=6pU5U5gAAAAJ&hl=en) (jahern@ucsd.edu) for use in the [Developmental Cognitive Neuroscience Lab at UCSD](https://greenelab.ucsd.edu/).
The tasks provided here are designed to be consistent with the movement task battery and action control coordination task used in previous work [(Gordon et. al. 2023)](https://doi.org/10.1038/s41586-023-05964-2)[^1]. Specific care has been taken to adapt these methods to a pediatric population and utilize guidelines identified in previous works [(Raschle et. al. 2009](https://doi.org/10.3791/1309) & [Wilke et. al. 2018)](https://doi.org/10.1002/acn3.658)[^2][^3]. 

-------------------------------------------------------------------------------------
## Left-Right Task 
[`Child_LeftRight_task.py`](https://github.com/j0n-a/fMRI_Pediatric_Movement_Battery/blob/main/Child_LeftRight_task.py)

This task is designed to establish a participant's ability to distinguish between the left and right sides of their body to establish minimum task competency prior to undertaking the full task in the MRI scanner. Stimuli are presented on the body and appear in one of four locations: the left hand, the right hand, the left foot, or the right foot. The body locations will be highlighted in either yellow or green. Participants will be asked to press the 'z' key if the left side of the body is highlighted and the 'm' key if the right side of the body is highlighted, and they must respond within 2 seconds. Participants will receive feedback on their responses. Brief pauses will be given after every 10 trials.

## Go/NoGo Task
[`Child_GoNoGo_task.py`](https://github.com/j0n-a/fMRI_Pediatric_Movement_Battery/blob/main/Child_GoNoGo_task.py)

Description of other tasks.

## Action Control Task
[`Child_ActionControl_task.py`](https://github.com/j0n-a/fMRI_Pediatric_Movement_Battery/blob/main/Child_ActionControl_task.py)

This task is a child version of Action Control Task from [(Gordon et. al. 2023)](https://doi.org/10.1038/s41586-023-05964-2)[^1]. There are three conditions for this task.

1) Body parts: left hand, right hand, left foot, right foot
2) Movements: left-right, clockwise, counterclockwise
3) Phases: plan (yellow arrow), execute (green arrow) - each up to 10 seconds

Body parts and Movements are randomized, but plan phase always comes first before execute phase. Participants will be asked to plan and execute based on the given stimuli and will receive feedback from the instructor on their responses. Brief pauses will be given after every 10 trials.

## Helper File
[`helper.py`](https://github.com/j0n-a/fMRI_Pediatric_Movement_Battery/blob/main/helper.py)

Helper functions used in other tasks. These functions include:
### `generate_trials(subj_code, seed, num_trials=48, task=None)`

This function generates trial lists used in the tasks. 
> - `subject_code`: A unique string to identify subjects.
> - `seed`: An integer that will be used as a basis for the pseudo-randomization used in the rest of the function.
> - `num_trials`: An integer representing the total number of stimuli you'd like to display during a task.
> - `task`: A string representing which task the trials are bing generated for. Valid inputs include `'LeftRight'`, `'GoNoGO'`, and `'ActionControl'`.

### `check_paths(current_directory, task=None)`
> - `current_directory`: A string representing the current full file path of the directory running the function.
> - `task`: A string representing which task the trials are bing generated for. Valid inputs include `'LeftRight'`, `'GoNoGO'`, and `'ActionControl'`.

-------------------------------------------------------------------------------------

Stimuli and associated information can be found in the [`stimuli` subfolder](https://github.com/j0n-a/fMRI_Pediatric_Movement_Battery/tree/main/stimuli).

[^1]: Gordon, E.M., Chauvin, R.J., Van, A.N. et. al. A somato-cognitive action network alternates with effector regions in motor cortex. Nature 617, 351–359 (2023). https://doi.org/10.1038/s41586-023-05964-2
[^2]: Raschle, N. M., Lee, M., Buechler, R., Christodoulou, J. A., Chang, M., Vakil, M., Stering, P. L., & Gaab, N. (2009). Making MR imaging child's play - pediatric neuroimaging protocol, guidelines and procedure. Journal of visualized experiments : JoVE, (29), 1309. https://doi.org/10.3791/1309
[^3]: Wilke, M., Groeschel, S., Lorenzen, A., Rona, S., Schuhmann, M.U., Ernemann, U. and Krägeloh-Mann, I. (2018), Clinical application of advanced MR methods in children: points to consider. Ann Clin Transl Neurol, 5: 1434-1455. https://doi.org/10.1002/acn3.658
