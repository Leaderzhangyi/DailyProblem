/*
 * @lc app=leetcode.cn id=86 lang=golang
 *
 * [86] 分隔链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func partition(head *ListNode, x int) *ListNode {
	dummy1 := &ListNode{0, nil}
	dummy2 := &ListNode{0, nil}

	p1, p2 := dummy1, dummy2
	p := head

	for p != nil {
		if p.Val >= x {
			p2.Next = p
			p2 = p2.Next
		} else {
			p1.Next = p
			p1 = p1.Next
		}
		p = p.Next
		// temp := p.Next
		// p.Next = nil
		// p = temp
	}
	p2.Next = nil // 判断有没有环
	p1.Next = dummy2.Next
	return dummy1.Next
}

// @lc code=end

