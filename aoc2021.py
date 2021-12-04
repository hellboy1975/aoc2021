import argparse
import shared
from shared import bcolours
import importlib

parser = argparse.ArgumentParser()
parser.add_argument("day",help = "The Day we want to process", type=int)
parser.add_argument("part",help = "Which part we're using", type=int)
parser.add_argument("--debug",help = "Will add some extra output to add to the confusion", action="store_true")
parser.add_argument("--sub",help = "Prints the sub", action="store_true")

args = parser.parse_args()

# this should really only ever be 1 or 2 - if it's not 2, make it one!
if args.part != 2:
    args.part = 1

print(f'Processing AOC2021 {bcolours.OKBLUE} Day: {args.day} Part: {args.part}{bcolours.ENDC}')

solution = f'day_{args.day}.part_{args.part}'

DEBUG = args.debug
if DEBUG:
    print('  Debug on!')

solutions_list = shared.getSolutions()

if args.sub:
    shared.printSubmarine()

if solution not in solutions_list:
    print(f'{bcolours.WARNING}This challenge hasn\'t been attempted yet.  Maybe some day....{bcolours.ENDC}')    
    exit()

try:
    if DEBUG:
        print(f'{solution} found!')    
    module = importlib.import_module(solution)
    thingo = module.Solution(DEBUG)
    thingo.run()
except Exception as e:
    print(f'  Exception! {bcolours.FAIL}{e}{bcolours.ENDC}')




