/*
 * @lc app=leetcode.cn id=203 lang=golang
 *
 * [203] 移除链表元素
 */

// @lc code=start

// type ListNode struct {
//     Val int
//     Next *ListNode
//  }

func removeElements(head *ListNode, val int) *ListNode {
	dummyHead := &ListNode{Next: head}

	tmp := dummyHead

	for tmp.Next != nil {
		if tmp.Next.Val == val {
			tmp.Next = tmp.Next.Next
		} else {
			tmp = tmp.Next
		}
	}
	return dummyHead.Next
}

// @lc code=end

