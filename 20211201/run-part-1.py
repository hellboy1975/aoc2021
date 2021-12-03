import argparse

print(f'Advent of Code 2021 Day 1 Part One')    

parser = argparse.ArgumentParser()

parser.add_argument("--debug",help = "Will add some extra output to add to the confusion")

args = parser.parse_args()

count = 0
previous = 0 
increasedCount = 0

# take the input file, and read it into an array
def fileToArray( file ):
    measurements = []
    data = open(file, 'r')
    lines = data.readlines()

    ## create and array of the measurements
    for line in lines:
        measurements.append(int(line))

    return measurements

measurements = fileToArray('data.txt')

for x in measurements:
    count += 1
    current = x
    
    if (count > 1):

        if (current > previous):
            status = 'increased'
            increasedCount += 1
        else:
            status = 'decreased'

        message = f'{current} ({previous}) {status}'
    else: 
        message = 'N/A - no previous sum'

    if (args.debug):
        print(f'{count}: {message}')
        
    previous = current

print(f'Total: {count}')    
print(f'Increased: {increasedCount}')