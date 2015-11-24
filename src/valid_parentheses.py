"""
Source : https://oj.leetcode.com/problems/valid-parentheses/
Author : Changxi Wu
Date   : 2015-01-20

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid 
but "(]" and "([)]" are not.

"""

def isValid( s):
    if not s:
        return False
    stack = []
    map = {'(':')', '[':']', '{':'}'}
    for c in s:
        if c in map.keys():
            stack.append(c)
        else:
            if len(stack) > 0:
                top = stack.pop()
                if map[top] != c:
                    return False
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    test_list = ['','(){}[]','({})','(',')',')(','()','([)]','([{])}']
    result_list = [0, 1, 1, 0, 0, 0, 1, 0, 0]
    success = True
    for i, s in enumerate(test_list):
        result = isValid(s)
        if result != result_list[i]:
            success = False
            print s
            print 'Expected value %d' % result_list[i]
            print 'Actual value %d' % result
    if success:
        print 'All the tests passed'
    else:
        print 'Please fix the failed test'
