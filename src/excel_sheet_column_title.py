"""
Source : https://oj.leetcode.com/problems/excel-sheet-column-number/
Author : Changxi Wu
Date   : 2015-01-21

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    732 -> ABC
"""

# @return a string
def convertToTitle(num):
    remainders = []
    quotient = num
    while quotient > 26:
        remainder = quotient%26 or 26
        quotient = (quotient-remainder)/26
        remainders.append(remainder)
    remainders.append(quotient)
    chars = []
    for i in reversed(remainders):
        chars.append(chr(i+ord('A')-1))
    return ''.join(chars)

if __name__ == '__main__':
    test = {1:'A', 2:'B', 3:'C', 26:'Z', 27:'AA', 28:'AB', 52:'AZ', 731:'ABC'}
    for k,v in test.iteritems():
        output = convertToTitle(k)
        if v != output:
            print 'Input:', k
            print 'Output:', output
            print 'Expected:', v
