"""
Source : https://oj.leetcode.com/problems/compare-version-numbers/
Author : Changxi Wu
Date   : 2015-01-23

Compare two version numbers version1 and version2.

if version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" for "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:
    0.1 < 1.1 < 1.2 < 13.37

"""

# @param version1, a string
# @param version2, a string
# @return an integer
def compareVersion(version1, version2):
    list1 = map(int, version1.split('.'))
    list2 = map(int, version2.split('.'))
    max_length = len(list1) if len(list1) > len(list2) else len(list2)
    for i in range(max_length):
        value1 = value2 = 0
        if i < len(list1):
            value1 = list1[i]
        if i < len(list2):
            value2 = list2[i]
        if value1 > value2:
            return 1
        elif value1 < value2:
            return -1
    return 0

if __name__ == '__main__':
    version1_list = ['0.1','1.1','1.2','13.37','1','1.0']
    version2_list = ['1.1','1.2','13.37','1','13.37','1.0']
    result_list = [-1, -1, -1, 1, -1, 0]
    max_length = len(version1_list)
    success = True
    for i in range(max_length):
        result = compareVersion(version1_list[i], version2_list[i])
        if result != result_list[i]:
            success = False
            print 'Input:', version1_list[i], version2_list[i]
            print 'Output:', result
            print 'Expected:', result_list[i]
    if success:
        print 'All tests are passed'

