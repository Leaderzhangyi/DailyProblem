/*
 * @lc app=leetcode.cn id=80 lang=golang
 *
 * [80] 删除有序数组中的重复项 II
 */

// @lc code=start
func removeDuplicates(nums []int) int {
	slow, fast := 2, 2
	if len(nums) < 3 {
		return len(nums)
	}
	for fast < len(nums) {
		if nums[fast] != nums[slow-2] {
			nums[slow] = nums[fast]
			slow++
		}
		fast++
	}
	return slow

}

// @lc code=end

