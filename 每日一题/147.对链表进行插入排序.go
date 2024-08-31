/*
 * @lc app=leetcode.cn id=147 lang=golang
 *
 * [147] 对链表进行插入排序
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func insertionSortList(head *ListNode) *ListNode {

	if head == nil {
		return nil
	}
	dummy := &ListNode{Next: head}
	lastSorted, curr := head, head.Next
	for curr != nil {
		if lastSorted.Val <= curr.Val {
			lastSorted = curr
		} else {
			prev := dummy
			for prev.Next.Val <= curr.Val {
				prev = prev.Next
			}
			lastSorted.Next = curr.Next
			curr.Next = prev.Next
			prev.Next = curr
		}
		curr = lastSorted.Next
	}
	return dummy.Next

}

// @lc code=end

