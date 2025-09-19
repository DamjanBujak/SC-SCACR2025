#!/usr/bin/env python3

#############
#  Imports  #
#############

# Common imports
import subprocess, csv, os
import dakota.interfacing as di

###################
#  Preprocessing  #
###################

# Get the Dakota Parameters and Response objects.
params, results = di.read_parameters_file()

# Substitute the parameter values into the templatized
# input file, outputting a valid input file for the 
# black-box code.
di.dprepro(template='eurotop-template.py', 
           parameters=params, 
           output='eurotop-run.py')

# Print the current working directory
print("Current Working Directory:", os.getcwd())

##################################
#  Running black-box simulation  #
##################################

result = subprocess.run('python eurotop-run.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# print("Output:", result.stdout)

# Print the current working directory
print("Ending ", os.getcwd())

# Importing results from simulation to Dakota
float_numbers = [float(number) for number in result.stdout.split()]

# Writing results to Dakota-formatted results file using the Response object.
results['overtop'].function = float_numbers[0]
results.write()