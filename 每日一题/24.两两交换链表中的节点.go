/*
 * @lc app=leetcode.cn id=24 lang=golang
 *
 * [24] 两两交换链表中的节点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
	dummy := &ListNode{0, head}
	cur := dummy
	for cur.Next != nil && cur.Next.Next != nil {
		a := cur.Next
		b := cur.Next.Next.Next
		cur.Next = cur.Next.Next
		cur.Next.Next = a
		cur.Next.Next.Next = b
		cur = cur.Next.Next
	}

	return dummy.Next

}

// @lc code=end

