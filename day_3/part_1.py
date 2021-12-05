import shared
import numpy

class Solution:
    def __init__(self, debug):
        self.debug = debug
        self.data = shared.fileToArray('day_3/data.txt')
        # self.data = shared.fileToArray('day_3/example.txt')

    def run(self):        
        gamma = epsilon = 0

        gamma, epsilon = self.workShitOut()

        print(f'Solution: {shared.bcolours.OKBLUE}{gamma * epsilon}{shared.bcolours.ENDC}')

    # determines the range by checking the length of the first element
    def getRange(self):
        return len(shared.stripNonNumeric(self.data[0])) 


    def workShitOut(self):
        count = 0
        bit_range = self.getRange()

        bit_totals = numpy.zeros([bit_range], dtype='int')

        for x in self.data:
            count += 1
            for i in range(0, bit_range):
                bit_totals[i] += int(x[i])

        print('Totals:')
        print(bit_totals)

        # TODO: I'm sure there's a better way to do this than concatonating strings :|
        gs = es = ''
        for y in bit_totals:
            if (y > (count / 2)):
                gs += '1'
                es += '0'
            else:
                gs += '0'
                es += '1'

        print(f'gamma: {shared.bcolours.OKGREEN}{gs}{shared.bcolours.ENDC} binary to int {shared.bcolours.OKGREEN}{int(gs,2)}{shared.bcolours.ENDC}')                
        print(f'epsilon: {shared.bcolours.OKGREEN}{es}{shared.bcolours.ENDC} binary to int {shared.bcolours.OKGREEN}{int(es,2)}{shared.bcolours.ENDC}')                

        return int(gs,2), int(es,2)


