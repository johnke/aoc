package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func part2(line string) int {
	score := 0
	currentContext := "do()"

	mulRegex := regexp.MustCompile(`mul\((\d+),(\d+)\)`) // Matches `mul(int,int)`
	mulMatches := mulRegex.FindAllStringSubmatchIndex(line, -1)

	contextRegex := regexp.MustCompile(`do\(\)|don't\(\)`) // Matches `do()` or `don't()`
	contextMatches := contextRegex.FindAllStringIndex(line, -1)

	contextIndex := 0

	for _, mulMatch := range mulMatches {
		for contextIndex < len(contextMatches) && contextMatches[contextIndex][0] < mulMatch[0] {
			if line[contextMatches[contextIndex][0]:contextMatches[contextIndex][1]] == "do()" {
				currentContext = "do()"
			} else {
				currentContext = "don't()"
			}
			contextIndex++
		}

		if currentContext == "do()" {
			a, _ := strconv.Atoi(line[mulMatch[2]:mulMatch[3]]) // First integer
			b, _ := strconv.Atoi(line[mulMatch[4]:mulMatch[5]]) // Second integer
			score += a * b
		}
	}
	return score
}

func part1(line string) int {
	score := 0
	re := regexp.MustCompile(`mul\((\d+),(\d+)\)`)

	matches := re.FindAllStringSubmatch(line, -1)

	for _, match := range matches {
		if len(match) == 3 {
			a, _ := strconv.Atoi(match[1])
			b, _ := strconv.Atoi(match[2])

			score += a * b
		}
	}
	return score
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

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	result := strings.Join(joined, "")
	fmt.Println("Part 1:", part1(result))
	fmt.Println("Part 2:", part2(result))
}

//// Part 1
// 188116424 - right
//// Part 2
// 104241938 - too low
// 104245808 - right
