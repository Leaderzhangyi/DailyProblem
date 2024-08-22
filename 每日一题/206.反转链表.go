/*
 * @lc app=leetcode.cn id=206 lang=golang
 *
 * [206] 反转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
	// var pre *ListNode
	// cur := head
	// for cur != nil {
	// 	next := cur.Next
	// 	cur.Next = pre
	// 	pre = cur
	// 	cur = next
	// }
	// return pre
	if head == nil || head.Next == nil {
		return head
	}
	p := reverseList(head.Next)
	head.Next.Next = head
	head.Next = nil
	return p

}

// @lc code=end

