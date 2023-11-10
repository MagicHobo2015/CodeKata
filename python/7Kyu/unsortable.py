# *******************************************************************************
# * Author: Joshua Land                                                         *
# * CodeWars: 7 kyu Sort the Unsortable                                         *
# *                                                                             *
# * Description: Given a list of integers and lists with a single integer, sort *
# *     the list as if they were all ints.                                      *
# *                                                                             *
# *******************************************************************************

# Brute Force Method.
# go through every element checking its type, looking for the smallest number.
# Move the smallest number to front of list.
# continue till the end. Basically selection sort so 0(n^2)


def sort_it(lst):
    lst.sort(key=lambda x: x[0] if type(x) == list else x)


def main():
    # Test Case One:
    one = [[3], 4, [2], [5], 1, 6]
    # one = [7,8,9,1,6,2,5,3,4]
    # Expected Results
    oneA = [1, [2], [3], 4, [5], 6]
    # oneA = [1,2,3,4,5,6,7,8,9]
    
    print(f'List starts out as:\t {one}')
    sort_it(one)
    print(f'List becomes: {one}')
    print(f'Expected: {oneA}')
    
    two = [[3], 7, [9], [5], 1, 6, [0]]
    # one = [7,8,9,1,6,2,5,3,4]
    # Expected Results
    twoA = [[0], 1, [3], [5], 6, 7, [9]]
    # oneA = [1,2,3,4,5,6,7,8,9]
    
    print(f'List starts out as:\t {two}')
    sort_it(two)
    print(f'List becomes: {two}')
    print(f'Expected: {twoA}')
    
    three = [[4], [1], [3]]
    # one = [7,8,9,1,6,2,5,3,4]
    # Expected Results
    threeA = [[1], [3], [4]]
    # oneA = [1,2,3,4,5,6,7,8,9]
    
    print(f'List starts out as:\t {two}')
    sort_it(two)
    print(f'List becomes: {two}')
    print(f'Expected: {twoA}')
    
if __name__ == "__main__":
    main()
    
    
    
    
# In this challenge you will be given a list similar to the following:

# [[3], 4, [2], [5], 1, 6]

# In words, elements of the list are either an integer or a list containing a single integer. If you try to sort this list via sorted([[3], 4, [2], [5], 1, 6]), Python will whine about not being able to compare integers and lists.

# However, us humans can clearly see that this list can reasonably be sorted according to "the content of the elements" as:

# [1, [2], [3], 4, [5], 6]

# Create a function that, given a list similar to the above, sorts the list according to the "content of the elements".

# Examples

# [4, 1, 3] ➞ [1, 3, 4]

# [[4], [1], [3]] ➞ [[1], [3], [4]]

# [4, [1], 3] ➞ [[1], 3, 4]

# [[4], 1, [3]] ➞ [1, [3], [4]]

# [[3], 4, [2], [5], 1, 6] ➞ [1, [2], [3], 4, [5], 6]
