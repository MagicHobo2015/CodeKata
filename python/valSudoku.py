# https://www.codewars.com/kata/540afbe2dc9f615d5e000425/train/python
from math import sqrt

class Sudoku(object):
    def __init__(self, data: list):
        self.data = data if len(data) > 0 else False

# self.data[row][col]
    def is_valid(self) -> bool:
        # get the length, check if its a square
        length = len(self.data)
        # if it is then continue working if its not the return false
        if sqrt(length).is_integer():
            # check that its not ragged        
            for li in self.data:
                if len(li) != length:
                    return False
            numToCheck = self.data[0][0]
            for col in range(0, length):
                for row in range(0, length):
                    if (numToCheck <= 0): return False

                    else:
                        return False
        else:
            return False

def main():
    goodSudoku1 = Sudoku([
      [7,8,4, 1,5,9, 3,2,6],
      [5,3,9, 6,7,2, 8,4,1],
      [6,1,2, 4,3,8, 7,5,9],
    
      [9,2,8, 7,1,5, 4,6,3],
      [3,5,7, 8,4,6, 1,9,2],
      [4,6,1, 9,2,3, 5,8,7],
      
      [8,7,6, 3,9,4, 2,1,5],
      [2,4,3, 5,6,1, 9,7,8],
      [1,9,5, 2,8,7, 6,3,4]
    ])

    goodSudoku2 = Sudoku([
      [1,4, 2,3],
      [3,2, 4,1],
    
      [4,1, 3,2],
      [2,3, 1,4]
    ])

    # Invalid Sudoku
    badSudoku1 = Sudoku([
      [0,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],

      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9]
    ])

    badSudoku2 = Sudoku([
      [1,2,3,4,5],
      [1,2,3,4],
      [1,2,3,4],
      [1]
    ])

    print("Should be good, good, false, false")
    print(goodSudoku1.is_valid())
    print(goodSudoku2.is_valid())
    print(badSudoku1.is_valid())
    print(badSudoku2.is_valid())

if __name__ == "__main__":
    main()