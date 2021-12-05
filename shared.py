# some shared code between day challenges

import importlib
import traceback
import re

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
    #TODO: maybe this could iterate the folders/files
    return [
        "day_1.part_1",
        "day_1.part_2",
        "day_2.part_1",
        "day_2.part_2",
        "day_3.part_1",
        "day_3.part_2"
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

def runSolution(solution, debug):
    try:
        if debug:
            print(f'{solution} found!')    
        module = importlib.import_module(solution)
        thingo = module.Solution(debug)
        thingo.run()
    except Exception as e:
        print(f'  Exception! {bcolours.FAIL}{e}{bcolours.ENDC}')
        print(traceback.format_exc())

# gets rid of pesky \n characters
def stripNonNumeric(s):
    foo = re.compile(r'[^\d.]+')
    return foo.sub('', s)        