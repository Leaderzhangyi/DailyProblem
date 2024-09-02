/*
 * @lc app=leetcode.cn id=200 lang=golang
 *
 * [200] 岛屿数量
 */

// @lc code=start

var dirs = [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func numIslands(grid [][]byte) int {
	ans := 0
	m := len(grid)
	n := len(grid[0])

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == '1' {
				ans++
				dfs(grid, i, j, m, n)
			}
		}
	}

	return ans
}
func dfs(grid [][]byte, i, j, m, n int) {

	grid[i][j] = '2'
	for _, d := range dirs {
		fx, fy := i+d[0], j+d[1]
		if 0 <= fx && fx < m && 0 <= fy && fy < n && grid[fx][fy] == '1' {
			dfs(grid, fx, fy, m, n)
		}
	}

}

// @lc code=end

