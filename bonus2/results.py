from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = Path('data')

# Iterate over all the CSV files in the data directory...
for file in DATA_DIR.iterdir():
	if file.suffix == '.csv':

		# Open the CSV file
		df = pd.read_csv(file)

		# Calculate accuracy for each number of dots
		accuracy_by_n_dots = df.groupby('n_dots')['correct'].mean()

		# Plot the results
		plt.plot(accuracy_by_n_dots.index, accuracy_by_n_dots)

plt.ylim(-0.05, 1.05)
plt.xlabel('Number of dots')
plt.ylabel('Accuracy')
plt.show()
