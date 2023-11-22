""" |*************************************************************************|
    |   Author: Joshua Land                                                   |
    |                                                                         |
    |   Discription: A simple set of unit tests for leet code challenge Roman |
    | Numerals.                                                               |
    |                                                                         |
    |                                                                         |
    |_________________________________________________________________________| """

from romanNumerals import RomanNumerals

def test_RomanNumerals():
    # list of numbers and their numeral 
    numerals = [1000, 4, 1, 1990, 2008, 21, 1, 4, 2008, 1666, 4000]
    answers = [ "M", "IV", "I", "MCMXC", "MMVIII", 'XXI', 'I', 'IV', 'MMVIII', 'MDCLXVI', 'MMMM' ]
    
    for numeral, answer in zip(numerals, answers):
        assert RomanNumerals.to_roman(numeral) == answer, "Broke on numerals to integers"