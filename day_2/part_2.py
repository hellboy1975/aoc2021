import sys
sys.path.append('../')
import shared

class Solution:
    def __init__(self, debug):
        self.debug = debug

    def run(self):
        commands = shared.fileToArray('day_2/data.txt')
        hPosition = depth = aim = count = 0

        # calculate the depth
        def calculateDepth(currentDepth, aim, distance):
            return currentDepth + (distance * aim)


        for command in commands:
            action, amount = command.strip().split(' ')
            amount = int(amount)

            if (self.debug):
                print(f'D: {depth} H: {hPosition} A: {aim}')
                print(f'Command: {action} {amount}')
                if count > 20:
                    break
                
            if (action == 'forward'):
                hPosition += amount
                depth = calculateDepth(depth, aim, amount)
            elif (action == 'down'):
                aim += amount     
            else:
                aim -= amount

            count += 1

        print(f'Total commands: {len(commands)}')
        print(f'Final Depth: {depth}')
        print(f'Final Horizontal position: {hPosition}')
        print(f'Final Horizontal * Final Depth =  {hPosition * depth}')