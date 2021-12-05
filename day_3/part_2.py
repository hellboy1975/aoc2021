import shared
import numpy

class Solution:
    def __init__(self, debug):
        self.debug = debug
        # self.data = shared.fileToArray('day_3/data.txt')
        self.data = shared.fileToArray('day_3/example.txt')

    def filterRating(self, common):
        matches = keep = []
        count = 0
        keep = self.data

        for b in format(common, 'b'):
            # print(f'Loop {count} |  b = {b}')
            # print(keep)
            for x in keep:
                x = shared.stripNonNumeric(x)
                # print(f'Consider [{x}] char {count}: {x[count]}')
                if x[count] == b:
                    # print(f'add {x} to matches')
                    matches.append(x)
            count += 1    

            # if we only have one item left we can bug out here
            if len(matches) == 1:
                print(f'MATCH: {count}: [{matches[0]}]')
                return int(matches[0],2)
            keep = matches
            print(f'KEEP: {count}: [{b}] {keep}')
            matches = []        

        # maybe, just maybe there will only be one left if we reach this point 🙏
        print(f'MATCH: {count}: {int(keep[0],2)}')
        return int(keep[0],2)

    def run(self):        
        oxy_common = co2_common = ''

        oxy_common, co2_common = self.getCommons()

        print('Oxy Rating ===')
        oxy_rating = self.filterRating(oxy_common)
        print('CO2 Rating ===')
        co2_rating = self.filterRating(co2_common)

        print(f'Solution: {shared.bcolours.OKGREEN}{oxy_rating} * {co2_rating}{shared.bcolours.ENDC} {shared.bcolours.OKBLUE}{oxy_rating * co2_rating}{shared.bcolours.ENDC}')

    # determines the range by checking the length of the first element
    def getRange(self):
        return len(shared.stripNonNumeric(self.data[0])) 

    def getCommons(self):
        """ Gets the common highest and lowest values in some kind of weird binary form for use in 
        poorly written submarine software

        Returns:
            int: returns two integers, the most common and least common
        """
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

        print(f'O2 generator binary: {shared.bcolours.OKGREEN}{gs}{shared.bcolours.ENDC}')                
        print(f'CO2 scrubber binary: {shared.bcolours.OKGREEN}{es}{shared.bcolours.ENDC}')                

        return int(gs,2), int(es,2)


