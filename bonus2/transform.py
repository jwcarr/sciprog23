from pathlib import Path
import json
import csv

DATA_DIR = Path('data')

# If the data directory does not yet exist, create it
if not DATA_DIR.exists():
    DATA_DIR.mkdir()

# Iterate over all the JSON files in the data directory...
for file_name in DATA_DIR.iterdir():
    if file_name.suffix == '.json':

        # Open the JSON file
        with open(file_name) as file:
            data = json.load(file)
        
        results = []

        # For each trial...
        for trial in data:
            if trial['trial_type'] == 'canvas-keyboard-response':
                n_dots = int(trial['n_dots'])
                response = int(trial['response'])
                correct = n_dots == response
                reaction_time = int(trial['rt'])
                results.append( [n_dots, response, correct, reaction_time] )

        output_file_name = file_name.with_suffix('.csv')

        csv_header = ['n_dots', 'response', 'correct', 'reaction_time']
        with open(output_file_name, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(csv_header)
            csv_writer.writerows(results)
