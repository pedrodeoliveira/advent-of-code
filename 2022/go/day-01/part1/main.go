package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {

	// open file
	f, err := os.Open("../../../days_inputs/day-01.txt")
	if err != nil {
		log.Fatal(err)
	}
	// remember to close the file at the end of the program
	defer f.Close()

	// read the file line by line using scanner
	scanner := bufio.NewScanner(f)

	elfMaxCalories := 0
	maxCalories := 0

	elf := 1
	calories := 0

	for scanner.Scan() {
		// do something with a line
		line := scanner.Text()

		// if line is empty, it terminated the calories for the current elf
		if line == "" {
			// increment number of elves and reset calories totalizer
			elf++
			calories = 0
		} else {
			calories, _ = strconv.Atoi(line)
			calories += calories
			// fmt.Printf("elf: %d with calories: %d\n", elf, elf_calories)

			if calories > maxCalories {
				maxCalories = calories
				elfMaxCalories = elf
				fmt.Printf("Found new elf %3d with max calories %5d\n", elf,
					maxCalories)
			}
		}
	}

	fmt.Printf("Terminated. The elf: %3d is the one with max calories %d\n",
		elfMaxCalories, maxCalories)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
