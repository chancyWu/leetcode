"""
Source : https://oj.leetcode.com/problems/merge-sorted-array/
Author : Changxi Wu
Date   : 2015-01-20

Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
    You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
"""

def merge(A, m, B, n):
    if len(A) == 0:
        A.extend(B)
        return

    previous = 0
    for b in B:
        for j in range(previous, len(A)):
            if b < A[j]:
                A.insert(j, b)
                previous = j+1
                break
            elif j == len(A)-1 and b > A[j]:
                A.append(b)
                previous = j+1
                break

if __name__ == '__main__':

    # test 1
    A1 = [3, 4, 6, 7]
    B1 = [1, 2, 5, 8, 9, 10]
    print "Input: ", A1, ',', B1
    merge(A1, len(A1), B1, len(B1))
    print "Output:", A1

    # test 2
    A2 = [3, 4, 6, 7]
    B2 = [8, 9]
    print "Input: ", A2, ',', B2
    merge(A2, len(A2), B2, len(B2))
    print "Output:", A2

    # test 3
    A3 = []
    B3 = [1]
    print "Input: ", A3, ',' , B3
    merge(A3, len(A3), B3, len(B3))
    print "Output:", A3

    # test 4
    A4 = []
    B4 = [1, 2, 4]
    print "Input: ", A4, ',' , B4
    merge(A4, len(A4), B4, len(B4))
    print "Output:", A4

    # test 5
    A5 = [8, 9]
    B5 = [1, 3, 5, 7]
    print "Input: ", A5, ',', B5
    merge(A5, len(A5), B5, len(B5))
    print "Output:", A5
