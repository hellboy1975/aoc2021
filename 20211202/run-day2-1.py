import sys
sys.path.append('../')
import shared

commands = shared.fileToArray('data.txt')
horizontal = depth = 0

for command in commands:
    action, amount = command.strip().split(' ')
    amount = int(amount)

    if (shared.args.debug):
        print(f'D: {depth} H: {horizontal}')
        print(f'Command: {action} {amount}')
    
    if (action == 'forward'):
        horizontal += amount
    elif (action == 'down'):
        depth += amount     
    else:
        depth -= amount

print(f'Total commands: {len(commands)}')
print(f'Final Depth: {depth}')
print(f'Final Horizontal position: {horizontal}')
print(f'Final Horizontal * Final Depth =  {horizontal * depth}')