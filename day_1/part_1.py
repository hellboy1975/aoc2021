import shared

class Solution:

    def __init__(self, debug):
        self.debug = debug

    def run(self):
        count = 0
        previous = 0 
        increasedCount = 0

        measurements = shared.fileToArray('day_1/data.txt')

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

            if (self.debug):
                print(f'{count}: {message}')
                
            previous = current

        print(f'Total: {count}')    
        print(f'Increased: {increasedCount}')