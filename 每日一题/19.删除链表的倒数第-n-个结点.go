/*
 * @lc app=leetcode.cn id=19 lang=golang
 *
 * [19] 删除链表的倒数第 N 个结点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {

	// dummy := &ListNode{0, head}
	// first, second := head, dummy
	// for i := 0; i < n; i++ {
	// 	first = first.Next
	// }
	// for ; first != nil; first = first.Next {
	// 	second = second.Next
	// }
	// second.Next = second.Next.Next
	// return dummy.Next

	dummy := &ListNode{0, head}
	// 经典快慢指针
	a := head
	for i := 0; i < n+1; i++ {
		if a == nil {
			return head.Next // 处理一下
		}
		a = a.Next
	}
	b := head
	for a != nil {
		a = a.Next
		b = b.Next
	}
	b.Next = b.Next.Next
	return dummy.Next

}

// @lc code=end

