import shared

class Solution:
    def __init__(self, debug):
        self.debug = debug

    def run(self):
        count = 0
        previous = 0 
        increasedCount = 0
        a = b = c = 0

        # the number of previous array items to include in the sum 
        itemsToSum = 2

        measurements = shared.fileToArray('day_1/data.txt')

        #TODO: make this loop less horrible
        for x in measurements:
            x = int(x)

            # need to treat the array in sets of three, so just skip the first couple of iterations
            if (count < 3):
                count += 1
                continue

            a = x
            if (count > 1):
                b = int(measurements[count - 1])

            if (count > 2):
                c = int(measurements[count - 2])

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

            if (self.debug):
                print(f'{count}: [{current}] {message}')
                
            previous = current
            count += 1

            if (self.debug) and (count > 20):
                break

        print(f'Dataset size: {count} records')    
        print(f'Increased: {increasedCount}')