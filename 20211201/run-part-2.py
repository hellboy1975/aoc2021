import argparse

print(f'Advent of Code 2021 Day 1 Part Two')    

parser = argparse.ArgumentParser()

parser.add_argument("--debug",help = "Will add some extra output to add to the confusion")

args = parser.parse_args()

count = 0
previous = 0 
increasedCount = 0
a = b = c = 0

# the number of previous array items to include in the sum 
itemsToSum = 2

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

#TODO: make this loop less horrible
for x in measurements:
    
    # need to treat the array in sets of three, so just skip the first couple of iterations
    if (count < 3):
        count += 1
        continue

    a = x
    if (count > 1):
        b = measurements[count - 1]

    if (count > 2):
        c = measurements[count - 2]        

    current = a + b + c

    if (count > 0):

        if (current > previous):
            status = 'increased'
            increasedCount += 1
        else:
            status = 'decreased'

        message = f' ({previous}) {status}'
    else: 
        message = 'N/A - no previous sum'

    if (args.debug):
        print(f'{count}: [{current}] {message}')
        
    previous = current
    count += 1

    if (args.debug) and (count > 20):
        break

print(f'Dataset size: {count} records')    
print(f'Increased: {increasedCount}')