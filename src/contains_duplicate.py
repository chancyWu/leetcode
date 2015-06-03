class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

if __name__ == '__main__':
    test_list = [[],[1],[1,1],[1,2],[1,2,3],[4,5,2,3,7,9,10,5],[4,3,5,2,6,7,10,1]]
    result_list = [False, False, True, False, False, True, False]
    success = True
    solution = Solution()
    for i,s in enumerate(test_list):
        result = solution.containsDuplicate(s)
        if result != result_list[i]:
            success = False
            print s
            print 'Expected value', result_list[i]
            print 'Actual value', result 
    if success:
        print 'All the tests passed'
    else:
        print 'Please fix the failed test'
