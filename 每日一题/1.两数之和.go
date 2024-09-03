/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	index := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		if idx, ok := index[target-nums[i]]; ok {
			return []int{i, idx}
		}
		index[nums[i]] = i
	}
	return []int{}
}

// @lc code=end

