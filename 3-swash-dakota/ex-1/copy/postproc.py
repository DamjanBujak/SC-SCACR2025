# Importing the necessary library
import numpy as np

# Constants for the file path
FILE_PATH = 'overtop.txt'

# Lists to store values
time = []
x_disch_values = []

# Reading the file and processing lines
with open(FILE_PATH, 'r') as file:
    for line in file:
        if line.startswith('%'):
            continue  # Skip comment lines
        parts = line.split()
        if len(parts) >= 2:  # Ensure the line has enough columns
            time.append(float(parts[0]))  
            x_disch_values.append(float(parts[3]))  
   
# Calculating and printing the mean if data is available
mean_x_disch = np.mean(x_disch_values)
print(mean_x_disch)
