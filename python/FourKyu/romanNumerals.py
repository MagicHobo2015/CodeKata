# ****************************************************************************\
# Author: Joshua Land                                                         *
#   Description: This is a couple of functions for converting Roman Numberals *
#       Back forth from integers and back to numerals                         *
#                                                                             *
#   Info: CodeWars - Roman Numerals Helper                                    *
#       Difficulty: 4 KYU                                                     *
# URL: https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python    *
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
        # This is similar to the correct change problem, so my first thought is .. greedy
        # there is a rule I overlooked about numbers to the right added and right subtracted.
        
        # Conversion table.
        numeral_map = { 1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}
        
        # To hold the results, and for readability
        results = ''
        



        return results



    @staticmethod
    def from_roman(roman_num : str) -> int:
        # TODO: algorithm here := ...
        return 0



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
        if pause:
            input("Press Return for next page")

# from before I was using pytest.
def main(debug):
    # Test Case Roman to Into
    one = ["M", "IV", "I", "MCMXC", "MMVIII"]
    oneA = [1000, 4, 1, 1990, 2008]
    
    # if debug == True:
    #     displayResults(one, oneA, RomanNumerals.from_roman)

    
    two = [21, 1, 4, 2008, 1666]
    twoA = ['XXI', 'I', 'IV', 'MMVIII', 'MDCLXVI']

    if debug:
        displayResults(two, twoA, RomanNumerals.to_roman)


# so this can be ran by itself.
if __name__ == '__main__':
    # need this to check command line args.
    import sys
    
    # Yay, Debug mode.
    if 'debug' in sys.argv:
        debug = True
    else:
        debug = False
    
    main( debug )
