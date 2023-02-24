#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node,val):
            if not node:
                return 0
            val = (val << 1) | node.val
            if not node.left and not node.right:
                return val
            return dfs(node.left,val) + dfs(node.right,val)
        return dfs(root,0)
# # # @lc code=end

