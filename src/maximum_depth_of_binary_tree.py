# Definition for a binary tree node
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

# normal recursive solution
# this recursive solution will call more methods which cause Time Limit Exceed
class Solution1:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root is None:
            return 0
        if self.left is None and self.right is None:
            return 1
        elif self.left is not None and self.right is not None:
            return self.maxDepth(self.left) + 1 if self.maxDepth(self.left) > \
                    self.maxDepth(self.right) else self.maxDepth(self.right) + 1
        elif self.left is not None:
            return self.maxDepth(self.left) + 1
        elif self.rigith is not None:
            return self.maxDepth(self.right) + 1

# recursive solution with only two methods call
# This is a cleaner solution with only two methods
# This is passed in the leetcode
class Solution2:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root is None:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return leftDepth + 1 if leftDepth > rightDepth else rightDepth + 1
