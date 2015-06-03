class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        stringLen = len(s)
        spaceIndex = 0
        wordIndex = 0
        spaceFound = False
        wordFound = False
        for i in range(0, len(s)):
            reverseIndex = stringLen - 1 - i
            if not wordFound:
                if s[reverseIndex] != ' ':
                    wordIndex = reverseIndex
                    wordFound = True
            elif s[reverseIndex] == ' ':
                spaceIndex = reverseIndex
                spaceFound = True
                break

        if spaceFound:
            return wordIndex-spaceIndex
        elif wordFound:
            return len(s)
        else:
            return 0

                   
if __name__ == '__main__':
    test_list = ['','a ','Hello world','abcdef','abc de f','abcd efg h ']
    result_list = [0,1,5,6,1,1]
    success = True
    solution = Solution()
    for i, s in enumerate(test_list):
        result = solution.lengthOfLastWord(s)
        if result != result_list[i]:
            success = False
            print s
            print 'Expected value', result_list[i]
            print 'Actual value', result
    if success:
        print 'All the tests passed'
    else:
        print 'Please fix the failed test'
