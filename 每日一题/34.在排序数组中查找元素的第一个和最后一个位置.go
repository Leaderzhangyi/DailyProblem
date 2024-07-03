/*
 * @lc app=leetcode.cn id=34 lang=golang
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 */
package main

// @lc code=start

func searchLeft(nums []int, target int) int {
	// 都写闭区间
	left, right := 0, len(nums)-1
	for left <= right {
		mid := left + (right-left)>>1
		if nums[mid] == target {
			right = mid - 1
		} else if nums[mid] > target {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	if left >= len(nums) || left < 0 {
		return -1
	}
	if nums[left] == target {
		return left
	}
	return -1

}

func searchRight(nums []int, target int) int {
	// 都写闭区间
	left, right := 0, len(nums)-1
	for left <= right {
		mid := left + (right-left)>>1
		if nums[mid] == target {
			left = mid + 1
		} else if nums[mid] > target {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	if left-1 >= len(nums) || left-1 < 0 {
		return -1
	}
	if nums[left-1] == target {
		return left - 1
	}
	return -1

}
func searchRange(nums []int, target int) []int {
	lp := searchLeft(nums, target)
	rp := searchRight(nums, target)

	return []int{lp, rp}
}

// @lc code=end
