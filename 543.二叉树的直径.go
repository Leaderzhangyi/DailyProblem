/*
 * @lc app=leetcode.cn id=543 lang=golang
 *
 * [543] 二叉树的直径
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func diameterOfBinaryTree(root *TreeNode) int {

	myMax := 0
	var maxDepth func(root *TreeNode) int
	maxDepth = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		leftmax := maxDepth(root.Left)
		Rightmax := maxDepth(root.Right)
		if leftmax+Rightmax > myMax {
			myMax = leftmax + Rightmax
		}
		return max(leftmax, Rightmax) + 1
	}
	maxDepth(root)
	return myMax

}

// @lc code=end

