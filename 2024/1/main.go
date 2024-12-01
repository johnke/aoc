package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func part1(list_left []int, list_right []int) int {
	var distance int
	var distance_total int

	if len(list_left) > 0 && len(list_right) > 0 {
		sort.Ints(list_left)
		sort.Ints(list_right)
		for i, val := range list_left {
			if list_right[i] > val {
				distance = list_right[i] - val
			} else {
				distance = val - list_right[i]
			}
			distance_total += distance
		}
	}
	return distance_total
}

func part2(list_left []int, list_right []int) int {
	var similarity int
	var similarity_total int

	if len(list_left) > 0 && len(list_right) > 0 {
		for _, val := range list_left {
			similarity = 0
			for _, valr := range list_right {
				if val == valr {
					similarity += 1
				}

			}
			fmt.Println(val, "occurs", similarity)
			similarity_total += val * similarity
		}
	}
	return similarity_total
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	var list_left []int
	var list_right []int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		vals := strings.Split(scanner.Text(), "   ")
		if val0, err := strconv.Atoi(vals[0]); err == nil {
			list_left = append(list_left, val0)
		}
		if val1, err := strconv.Atoi(vals[1]); err == nil {
			list_right = append(list_right, val1)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("Part 1", part1(list_left, list_right))
	fmt.Println("Part 2", part2(list_left, list_right))
}

// part 1 - 1722302
// part 2 - 20373490
