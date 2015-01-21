"""
Source : https://oj.leetcode.com/problems/excel-sheet-column-number/
Author : Changxi Wu
Date   : 2015-01-21

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
     A -> 1
     B -> 2
     C -> 3
     ...
     Z -> 26
     AA -> 27
     AB -> 28 

"""


def titleToNumber(s):
    # @praram s, a string
    # @return an integer
    result = 0
    length = len(s)
    for i, c in enumerate(s):
        if length == 1:
            result += (ord(c)-ord('A')+1)
        else:
            result += (ord(c)-ord('A')+1)*(26**(length-i-1))
    return result 

    

if __name__ == '__main__':
    test = {'A':1, 'B':2, 'C':3, 'D':4, 'AA':27, 'AB':28, 'ABC':731}
    
    for s in test.keys():
        result = titleToNumber(s)
        if result != test[s]:
            print 'Input: ', s
            print 'Output:', result
            print 'Expected:', test[s]
