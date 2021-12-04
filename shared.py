# some shared code between day challenges

import array

# take the input file, and read it into an array
def fileToArray( file ):
    measurements = []
    data = open(file, 'r')
    lines = data.readlines()

    ## create and array of the measurements
    for line in lines:
        measurements.append(line)

    return measurements

# prints the Sub!
def printSubmarine():
    print ("""
                                 o o
                                 o ooo
                                   o oo
                                      o o      |   #)
                                       oo     _|_|_#_
                                         o   | AOC21 |
    __                    ___________________|       |_________________
   |   -_______-----------                                              \\
  >|    _____                                                   --->     )
   |__ -     ---------_________________________________________________ /
    """)    

# returns a list of solutions I've added
def getSolutions():
    return [
        "day_1.part_1",
        "day_1.part_2",
        "day_2.part_1",
        "day_2.part_2"
        ]

class bcolours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[90m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'        
    # Background colors:
    GREYBG = '\033[100m'
    REDBG = '\033[101m'
    GREENBG = '\033[102m'
    YELLOWBG = '\033[103m'
    BLUEBG = '\033[104m'
    PINKBG = '\033[105m'
    CYANBG = '\033[106m'