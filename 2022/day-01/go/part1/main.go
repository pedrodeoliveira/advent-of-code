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
	f, err := os.Open("../../input.txt")
	if err != nil {
		log.Fatal(err)
	}
	// remember to close the file at the end of the program
	defer f.Close()

	// read the file line by line using scanner
	scanner := bufio.NewScanner(f)

	elf_most_calories := 0
	most_calories := 0

	elf := 1
	elf_calories := 0

	for scanner.Scan() {
		// do something with a line
		line := scanner.Text()

		// terminated calories for elf, check if elf with most calories needs
		// to be updated
		if line == "" {
			if elf_calories > most_calories {
				most_calories = elf_calories
				elf_most_calories = elf
				fmt.Printf(" >>> new elf: %d with most calories: %d\n", elf_calories,
					most_calories)
			}

			// increment number of elves and reset calories totalizer
			fmt.Printf("finished inventory for elf %d with total calories %d\n", elf,
				elf_calories)
			elf++
			elf_calories = 0
		} else {
			calories, _ := strconv.Atoi(line)
			elf_calories += calories
			fmt.Printf("elf: %d with calories: %d\n", elf, elf_calories)
		}
	}

	// process last elf
	if elf_calories != 0 {
		fmt.Printf("finished inventory for elf %d with total calories %d\n", elf,
			elf_calories)
		if elf_calories > most_calories {
			most_calories = elf_calories
			elf_most_calories = elf
			fmt.Printf(" >>> new elf: %d with most calories: %d\n", elf_calories,
				most_calories)
		}
	}

	fmt.Printf("[results] elf: %d with calories: %d\n", elf_most_calories, most_calories)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
