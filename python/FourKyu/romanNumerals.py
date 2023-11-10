# ****************************************************************************\
# Author: Joshua Land                                                         *
#   Description: This is a couple of functions for converting Roman Numberals *
#       Back forth from integers and back to numerals                         *
#                                                                             *
#   Info: CodeWars - Roman Numerals Helper                                    *
#       Difficulty: 4 KYU                                                     *
# ****************************************************************************/



class RomanNumerals:
    
    @staticmethod
    def to_roman(val : int) -> str:
        """A function to convert 0 <= integers <= 4000 into Roman Numerals.

        Args:
            val (int): An integer to be converted to roman numerals

        Returns:
            str: The roman numeral representation of the integer that was input.
        """
        # This is similar to the correct change problem, so my first thought is .. stack?
        
        # My First Pass is going to use this, call it brute force.
        numeral_map = { 1 : 'I', 4 : 'IV', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}
        
        # To hold the results, and for readability
        results = ''
        
        # now I need a sentinal
        number = val
        
        # Start a loop through master list in reverse order because we want greatest to smalles.
        for thing in reversed(numeral_map):
            # this will loop untill current denomination is to big.
            while ( number > thing ):
                # subtract one denomination from the sentinal
                number -= thing
                # new results holder
                numToNum = numeral_map[thing]
                
            number = 0
        
        
        return ''



    @staticmethod
    def from_roman(roman_num : str) -> int:
        # TODO: algorithm here := ...
        return 0





'''
Symbol 	Value
I 	1
IV 	4
V 	5
X 	10
L 	50
C 	100
D 	500
M 	1000
'''


def displayResults(questions: list, answers: list, function_To_Run):
    
    # this is just to paginate the results
    pause = True
    
    # loop through the lists, run the function on them and display what comes out.    
    for testCase, answer in zip(questions, answers):
        results = function_To_Run(testCase)
        
        print("-" * 80)
        print(f'Testing:\t {testCase} \n')
        print(f'{testCase} Should become: {answer}\n')
        
        print(f'Actual Results were:\t {results}\n')
        
        print("-" * 80)

# from before I was using pytest.
def main():
    # Test Case Roman to Int
    one = ["M", "IV", "I", "MCMXC", "MMVIII"]
    oneA = [1000, 4, 1, 1990, 2008]
    
    displayResults(one, oneA, RomanNumerals.from_roman)

    
    two = [21, 1, 4, 2008, 1666]
    twoA = ['XXI', 'I', 'IV', 'MMVIII', 'MDCLXVI']

    displayResults(two, twoA, RomanNumerals.to_roman)
    

# so this can be ran by itself.
if __name__ == '__main__':
    # main()
    pass