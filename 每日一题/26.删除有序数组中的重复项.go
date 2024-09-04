/*
 * @lc app=leetcode.cn id=26 lang=golang
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
func removeDuplicates(nums []int) int {
	// dict := make(map[int]bool)
	// i, j := 0, 0
	// for j < len(nums) {
	// 	if !dict[nums[j]] {
	// 		dict[nums[j]] = true
	// 		nums[i] = nums[j]
	// 		i++
	// 	}
	// 	j++
	// }
	// return i
	if len(nums) == 0 {
		return 0
	}
	slow := 1
	for fast := 1; fast < len(nums); fast++ {
		if nums[fast] != nums[slow-1] {
			nums[slow] = nums[fast]
			slow++
		}
	}
	return slow

}

// @lc code=end

