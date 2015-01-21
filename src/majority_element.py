"""
Source : https://oj.leetcode.com/problems/majority-element/
Author : Changxi Wu
Date   : 2015-01-21

Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

# @param num, a list of integers
# @return an integer
def majorityElement( num):
    d = dict((e1, 0) for e1 in set(num))
    half_length = len(num)/2
    for n in num:
        d[n] += 1
        if d[n] > half_length:
            return n


if __name__ == '__main__':
    list1 = [1, 1, 2, 1, 2]
    result1 = 1
    print 'Input:', list1
    result = majorityElement(list1)
    print 'Output:', result1
