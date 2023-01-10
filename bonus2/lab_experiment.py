from psychopy import core, event, monitors, visual, gui
from pathlib import Path
import random
import csv

####################################################
# Experiment parameters
####################################################

DATA_DIR = Path('data')
SCREEN_SIZE = (1512, 982) # <- PUT YOUR SCREEN RESOLUTION HERE
WINDOW_SIZE = (800, 600)
FULLSCREEN_MODE = False

DOT_RADIUS = 10
MIN_DOTS = 1
MAX_DOTS = 9
N_REPS = 1

####################################################
# Preparation
####################################################

# Ask for the subject ID
subject_number_dialog = gui.Dlg('Count the dots')
subject_number_dialog.addField('Subject ID:')
subject_id = subject_number_dialog.show()[0]

# Determine file path where data will be stored
output_file_path = DATA_DIR / f'{subject_id}.csv'

# If the data directory does not yet exist, create it
if not DATA_DIR.exists():
    DATA_DIR.mkdir()

# Check if the file already exists (if so, raise an error)
if output_file_path.exists():
    raise ValueError('This subject ID already exists')

# Create the monitor object and set the screen resolution
monitor = monitors.Monitor('monitor')
monitor.setSizePix(SCREEN_SIZE)

# Create a new window on the monitor
window = visual.Window(
    size=WINDOW_SIZE,
    monitor=monitor,
    fullscr=FULLSCREEN_MODE,
    winType='pyglet',
    units='pix',
    allowStencil=True,
    color=(1, 1, 1)
)

# Create the instruction texts
instruction_text = visual.TextStim(window, color='black', text='''You will see some dots for a short amount of time.
Your task is to estimate how many dots you saw.
Try to be as accurate as possible.

Press SPACE to begin''')
how_many_text = visual.TextStim(window, color='black', text=f'How many dots? [{MIN_DOTS}–{MAX_DOTS}]')
finished_text = visual.TextStim(window, color='black', text='Experiment complete')

# Create the dot stimulus
dot = visual.Circle(window, lineColor='black', fillColor='black', radius=DOT_RADIUS, lineWidth=1)

# Calculate area in which dots can be displayed
window_width = WINDOW_SIZE[0]
window_height = WINDOW_SIZE[1]

half_window_width = WINDOW_SIZE[0] // 2
half_window_height = WINDOW_SIZE[1] // 2

min_x_pos = -half_window_width + DOT_RADIUS
max_x_pos = half_window_width - DOT_RADIUS

min_y_pos = -half_window_height + DOT_RADIUS
max_y_pos = half_window_height - DOT_RADIUS

# Generate the trials
trials = []
for n in range(MIN_DOTS, MAX_DOTS + 1):
    trials.extend([n] * N_REPS)
random.shuffle(trials)

# Empty list where results will be stored
results = []

####################################################
# Main experiment script
####################################################

# Show the instructions and await SPACE key
instruction_text.draw()
window.flip()
event.waitKeys(keyList=['space'])
window.flip()

# For each trial...
for n_dots in trials:

    # For each of the dots on this trial...
    for _ in range(n_dots):
        # Pick a random position and draw the dot in that position
        rand_pos_x = random.randint(min_x_pos, max_x_pos)
        rand_pos_y = random.randint(min_y_pos, max_y_pos)
        dot.pos = (rand_pos_x, rand_pos_y)
        dot.draw()

    # Reveal the dots
    window.flip()
    # Wait 500ms
    core.wait(0.5)
    # Remove the dots
    window.flip()

    # Ask the participant for a response and wait for them to press a number key
    how_many_text.draw()
    window.flip()
    pressed_keys = event.waitKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    window.flip()

    # Get the participants response and store whether or not it was correct
    response = int(pressed_keys[0])
    correct = n_dots == response
    results.append( (n_dots, response, correct) )

    # Wait 500ms before proceeding to the next trial
    core.wait(0.5)

# Display the end of experiment text and wait for the SPACE key
finished_text.draw()
window.flip()
event.waitKeys(keyList=['space'])

####################################################
# Save the results
####################################################

csv_header = ['n_dots', 'response', 'correct']

with open(output_file_path, 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_header)
    csv_writer.writerows(results)
