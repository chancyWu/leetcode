"""
Source : https://oj.leetcode.com/problems/merge-sorted-array/
Author : Changxi Wu
Date   : 2015-01-20

Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
    You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
"""

def merge(A, m, B, n):
    for b in B:
        previous = 0
        if len(A) == 0:
            A.append(b)
        else:
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
    print A1
    print B1
    merge(A1, len(A1), B1, len(B1))
    print 'Merged:'
    print A1

    # test 2
    A2 = [3, 4, 6, 7]
    B2 = [8, 9]
    print A2
    print B2
    merge(A2, len(A2), B2, len(B2))
    print 'Merged:'
    print A2

    # test 3
    A3 = []
    B3 = [1]
    print A3
    print B3
    merge(A3, len(A3), B3, len(B3))
    print 'Merged:'
    print A3
