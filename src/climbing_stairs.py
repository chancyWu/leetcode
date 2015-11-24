class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fn_1 = 1
        fn_2 = 2
        if n == 1:
            return fn_1
        if n == 2:
            return fn_2

        for i in range(3, n+1):
            fn = fn_1 + fn_2
            fn_1 = fn_2
            fn_2 = fn
        return fn
