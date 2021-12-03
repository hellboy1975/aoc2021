# some shared code between day challenges

import argparse

print(f'Advent of Code 2021 Day 2 Part One')    

parser = argparse.ArgumentParser()

parser.add_argument("--debug",help = "Will add some extra output to add to the confusion")

args = parser.parse_args()


# take the input file, and read it into an array
def fileToArray( file ):
    measurements = []
    data = open(file, 'r')
    lines = data.readlines()

    ## create and array of the measurements
    for line in lines:
        measurements.append(line)

    return measurements