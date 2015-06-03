class Solution:
    # @param {string []} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        longestIndex = 0
        foundNotMatched = False
        for index in range(0, len(strs[0])):
            if not foundNotMatched:
                longestIndex = index
                char = strs[0][index]
                for i,str in enumerate(strs):
                    if index >= len(str) or str[index] != char:
                        foundNotMatched = True
                        break
        if foundNotMatched:
            return strs[0][:longestIndex]
        else:
            return strs[0][:longestIndex+1]


if __name__ == '__main__':
    test_list = [[], ['a'], ['a','b'], ['aa','aa'], ['aa', 'a']]
    result_list = ['','a','','aa','a']
    success = True
    solution = Solution() 
    for i, s in enumerate(test_list):
        result = solution.longestCommonPrefix(s)
        if result != result_list[i]:
            success = False
            print s
            print 'Expected value ',result_list[i]
            print 'Actual value ',result
    if success:
        print 'All the tests passed'
    else:
        print 'Please fix the failed test'
