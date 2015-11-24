class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        amount = 0
        for i, c in enumerate(s):
            cur = self.romanTable(c)
            if i < len(s)-1:
                nex = self.romanTable(s[i+1])
                if cur >= nex:
                    amount = amount + cur
                else:
                    amount = amount - cur
            else:
                amount = amount + cur
        return amount

    def romanTable(self, c):
        return {
                'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000,
        }.get(c, 0)

if __name__ == '__main__':
    s_list = ['MCMIV', 'MCMLIV', 'MCMXC', 'MMXIV', 'DCXXI']
    result_list = [1904, 1954, 1990, 2014, 621]
    success = True
    solution = Solution()
    for i in range(len(s_list)):
        result = solution.romanToInt(s_list[i])
        if result != result_list[i]:
            print s_list[i]
            print 'current', result
            print 'expected', result_list[i]
            success = False
    if success:
        print 'All passed'
