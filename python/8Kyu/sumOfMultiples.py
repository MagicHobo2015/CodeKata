# |---------------------------------------------------------------------------\
# | Author: Joshua Land                                                       |
# |     Diffuculty: 8 kyu                                                     |
# | Description: Sum of Multiples - sum multiples of n upto m.                |
# |---------------------------------------------------------------------------/

def sum_mul(n, m):
    return "INVALID" if (m <= 0 or n <= 0) else sum(range( 0, m, n ))




def main():
    test_numbers = [(2,9), (3, 13), (4, 123), (4, -7)]
    expected = [20, 30, 1860, 'INVALID']

    # sumMul(2,9) = 20
    results = sum_mul(2, 9)
    result_str = f'Testing...\t (2, 9) \n OutPut:\t { results } \n Expected: \t 20'

    print('-' * 79)
    print(result_str)
    print('-' * 79 + '\n')


    # sumMul(3, 13) = 30
    results = sum_mul(3, 13)
    result_str = f'Testing...\t (3, 13) \n OutPut:\t { results } \n Expected: \t 30'
    
    print('-' * 79)
    print(result_str)
    print('-' * 79 + '\n')


    # sumMul(2,9) = 1860
    results = sum_mul(4, 123)
    result_str = f'Testing...\t (4, 123) \n OutPut:\t { results } \n Expected: \t 1860'

    print('-' * 79)
    print(result_str)
    print('-' * 79 + '\n')

    # sumMul(2,9) = "INVALID"
    results = sum_mul(4, -7)
    result_str = f'Testing...\t 4, -7 \n OutPut:\t { results } \n Expected: \t "INVALID"'

    print('-' * 79)
    print(result_str)
    print('-' * 79 + '\n')


if __name__ == '__main__':
    main()



'''
sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sumMul(4, -7)  ==> "INVALID"

'''