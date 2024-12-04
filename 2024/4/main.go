package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func part2(grid []string) int {
	rows := len(grid)
	cols := len(grid[0])
	count := 0

	checkDiagonalMAS := func(x, y int) bool {
		if x-1 >= 0 && x+1 < rows && y-1 >= 0 && y+1 < cols {
			topLeft := string(grid[x-1][y-1])
			topRight := string(grid[x-1][y+1])
			bottomLeft := string(grid[x+1][y-1])
			bottomRight := string(grid[x+1][y+1])

			// lol brute force
			if topLeft == "M" && topRight == "S" && bottomLeft == "M" && bottomRight == "S" {
				return true
			}
			if topLeft == "S" && topRight == "M" && bottomLeft == "S" && bottomRight == "M" {
				return true
			}
			if topLeft == "M" && topRight == "M" && bottomLeft == "S" && bottomRight == "S" {
				return true
			}
			if topLeft == "S" && topRight == "S" && bottomLeft == "M" && bottomRight == "M" {
				return true
			}

		}
		return false
	}

	// Iterate over each cell in the grid
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if grid[i][j] == 'A' {
				if checkDiagonalMAS(i, j) {
					count++
				}
			}
		}
	}
	return count
}

func part1(grid []string) int {
	rows := len(grid)
	cols := len(grid[0])
	count := 0
	directions := [][]int{
		{0, 1},   // right
		{0, -1},  // left
		{1, 0},   // down
		{-1, 0},  // up
		{1, 1},   // diagonal down-right
		{-1, -1}, // diagonal up-left
		{-1, 1},  // diagonal up-right
		{1, -1},  // diagonal down-left
	}

	target := "XMAS"
	targetLen := len(target)

	// Helper function to check if a word matches in a direction
	checkDirection := func(x, y, dx, dy int) bool {
		for k := 0; k < targetLen; k++ {
			nx, ny := x+k*dx, y+k*dy
			if nx < 0 || nx >= rows || ny < 0 || ny >= cols || grid[nx][ny] != target[k] {
				return false
			}
		}
		return true
	}

	// Iterate over each cell in the grid
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			for _, dir := range directions {
				dx, dy := dir[0], dir[1]
				if checkDirection(i, j, dx, dy) {
					count++
				}
			}
		}
	}

	return count
}

func main() {
	if len(os.Args) != 2 {
		log.Fatal("Usage: program filename")
	}

	filename := os.Args[1]
	file, err := os.Open(filename)

	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)
	joined := []string{}
	for scanner.Scan() {
		joined = append(joined, scanner.Text())
	}

	defer file.Close()

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(joined)
	fmt.Println("Part 1:", part1(joined))
	fmt.Println("Part 2:", part2(joined))
}

//// Part 1
// 2458 - Correct

//// Part 2
// 2003 - Too high
// 1945 - Correct
