/*
 * @lc app=leetcode.cn id=209 lang=golang
 * @lcpr version=20001
 *
 * [209] 长度最小的子数组
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
func minSubArrayLen(target int, nums []int) int {
	n := len(nums)
	res := n + 1
	flagSum := 0
	left := 0
	for right, num := range nums {
		flagSum += num
		for flagSum >= target {
			res = min(res, right-left+1)
			flagSum -= nums[left]
			left++
		}
	}
	if res <= n {
		return res
	} else {
		return 0
	}

}

// @lc code=end

/*
// @lcpr case=start
// 7\n[2,3,1,2,4,3]\n
// @lcpr case=end

// @lcpr case=start
// 4\n[1,4,4]\n
// @lcpr case=end

// @lcpr case=start
// 11\n[1,1,1,1,1,1,1,1]\n
// @lcpr case=end

*/

