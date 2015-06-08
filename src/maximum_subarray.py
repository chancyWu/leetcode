# brute force solution
# it works, but Time Limit Exceeded in leetcode
class Solution1:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if not nums:
            return None
        maxSum = nums[0]
        for size in range(1, len(nums)+1):
            for i in range(0, len(nums)+1-size): 
                # print nums[i:i+size]
                curSum = sum(nums[i:i+size])
                if curSum > maxSum:
                    maxSum = curSum
        return maxSum


if __name__ == '__main__':
    test_list = [[-2, 1, -3, 4, -1, 2, 1, -5, 4]]
    result_list = [6]
    success = True
    solution = Solution1()
    for i,nums in enumerate(test_list):
        result = solution.maxSubArray(nums)
        if result != result_list[i]:
            success = False
            print nums
            print 'Expected value', result_list[i]
            print 'Actual value', result
    if success:
        print 'All the tests passed'
    else:
        print 'Please fix the failed test'
