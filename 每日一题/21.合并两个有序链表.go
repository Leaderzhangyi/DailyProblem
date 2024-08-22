/*
 * @lc app=leetcode.cn id=21 lang=golang
 *
 * [21] 合并两个有序链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	dummpy := &ListNode{0, nil}
	p := dummpy
	a := list1
	b := list2

	for a != nil && b != nil {
		if a.Val <= b.Val {
			p.Next = a
			a = a.Next
		} else {
			p.Next = b
			b = b.Next
		}
		p = p.Next
	}
	if a != nil {
		p.Next = a

	}
	if b != nil {
		p.Next = b
	}
	return dummpy.Next

}

// @lc code=end

