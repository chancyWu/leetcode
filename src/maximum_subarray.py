# brute force solution O(n^3)
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

# Improved brute force solution with prefix sum array O(n^2)
# though it's better solution, but still Time Limit Exceeded in leetcode
class Solution2:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if not nums:
            return None
        # convert array nums to prefix sum array
        for i,num in enumerate(nums):
            if i == 0:
                continue
            else:
                nums[i] = nums[i] + nums[i-1]
        # enumerate the sub array
        maxSum = nums[0]
        for size in range(1, len(nums)+1):
            for i in range(0, len(nums) -size):
                curSum = nums[i+size] - nums[i]
                if curSum > maxSum:
                    maxSum = curSum
        return maxSum

# Dynamic Programming with state transaction. O(n)
# cur_sum = max(a[i], cur_sum + a[i]) ?? think about this.
# max_sum = max(cur_sum, max_sum)
class Solution3:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if not nums:
            return None
        for i, num in enumerate(nums):
            if i == 0:
                cur_sum = nums[0]
                max_sum = cur_sum
            else:
                cur_sum = num if num > cur_sum + num else cur_sum + num
                max_sum = cur_sum if cur_sum > max_sum else max_sum
        return max_sum

if __name__ == '__main__':
    test_list = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [-1]]
    result_list = [6, 1, -1]
    success = True
    solution = Solution3()
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
