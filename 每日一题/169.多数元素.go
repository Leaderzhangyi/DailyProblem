
/*
 * @lc app=leetcode.cn id=169 lang=golang
 *
 * [169] 多数元素
 */

// @lc code=start
func majorityElement(nums []int) int {
	// if len(nums) == 1 {
	// 	return nums[0]
	// }
	// dict := make(map[int]int)
	// flag := len(nums) / 2
	// for _, num := range nums {
	// 	dict[num]++
	// 	if dict[num] > flag {
	// 		return num
	// 	}
	// }
	// return 0

	// 摩尔投票法
	count := 0
	var op, res int

	for _, num := range nums {
		if count == 0 {
			res = num
		}
		if num == res {
			op = 1
		} else {
			op = -1
		}
		count += op
	}
	return res

}

// @lc code=end

