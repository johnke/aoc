package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strings"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func get_increasing_decreasing(reports [][]int) [][]int {
	var safe_reports [][]int
	for _, report := range reports {
		nums_sorted_a := slices.Clone(report)
		nums_sorted_d := slices.Clone(report)
		slices.Sort(nums_sorted_a)
		slices.Sort(nums_sorted_d)
		slices.Reverse(nums_sorted_d)

		areEqual_a := slices.Equal(report, nums_sorted_a)
		areEqual_d := slices.Equal(report, nums_sorted_d)
		if areEqual_a || areEqual_d {
			safe_reports = append(safe_reports, report)
		}
	}
	return safe_reports
}

func get_safe_report(report []int) bool {
	is_safe := true
	for i, val := range report {
		if i < len(report)-1 {
			diff := abs(val - report[i+1])
			if diff > 3 || diff < 1 {
				is_safe = false
			}
		}
	}
	return is_safe
}

func part1(reports [][]int) int {
	safe := 0
	inc_dec_reports := get_increasing_decreasing(reports)
	for _, report := range inc_dec_reports {
		is_safe := get_safe_report(report)
		if is_safe {
			safe++
		}
	}
	return safe
}

func is_ordered(report []int) bool {
	nums_sorted_a := slices.Clone(report)
	nums_sorted_d := slices.Clone(report)
	slices.Sort(nums_sorted_a)
	slices.Sort(nums_sorted_d)
	slices.Reverse(nums_sorted_d)

	areEqual_a := slices.Equal(report, nums_sorted_a)
	areEqual_d := slices.Equal(report, nums_sorted_d)
	if areEqual_a || areEqual_d {
		return true
	} else {
		return false
	}
}

func is_safe(report []int) bool {
	for i, val := range report {
		if i < len(report)-1 {
			diff := abs(val - report[i+1])
			if diff > 3 || diff < 1 {
				return false
			}
		}
	}
	if is_ordered(report) {
		return true
	}
	return false
}

func part2(reports [][]int) int {
	var safe_reports [][]int
	for _, report := range reports {
		for i := 0; i < len(report); i++ {
			temp_report := slices.Clone(report)
			temp_report = append(temp_report[:i], temp_report[i+1:]...)
			if is_safe(temp_report) {
				safe_reports = append(safe_reports, temp_report)
				break
			}
		}
	}

	return len(safe_reports)
}

func main() {
	if len(os.Args) != 2 {
		log.Fatal("Usage: program filename")
	}

	var reports [][]int

	filename := os.Args[1]
	file, err := os.Open(filename)

	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		s := strings.Split(scanner.Text(), " ")
		var nums []int
		for _, val := range s {
			n := 0
			fmt.Sscanf(val, "%d", &n)
			nums = append(nums, n)
		}
		reports = append(reports, nums)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("Part 1:", part1(reports))
	fmt.Println("Part 2:", part2(reports))

}

//// Part 1
// 706 - too high
// 202 - right

//// Part 2
// 265 - too low
// 333 - too high
// 271 - right
