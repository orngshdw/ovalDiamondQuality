/* main program

User enters the Table %, Depth %, length, and width numbers to get diamond quality.

Quality: Excellent, Very Good,              Good,                   Fair,                   Poor
Table%:  53-63,     52 or 64-65,            51 or 66-68,            50 or 69-70,            <50 or >70
Depth%:  58-62,     56-57.9 or 62.1-66,     53-55.9 or 66.1-71,     50-52.9 or 71.1-74,     <50 or >74
Len/Wid: 1.35-1.50, 1.30-1.34 or 1.51-1.55, 1.25-1.29 or 1.56-1.60, 1.20-1.24 or 1.61-1.65, <1.20 or >1.65

Reference: https://www.diamonds.pro/education/oval-cut/
Creator: Kenny Hoang
MIT License
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const inputErrMsg = "Please enter a number between 0 and 100"

func OvalQuality() {
	quality := []string{"Poor", "Fair", "Good", "Very Good", "Excellent"}
	// Create an array of keys so that we can use it to iterate through map in order
	referenceKeys := [3]string{"table", "depth", "length_width"}
	reference := map[string][]float64{
		"table": []float64{50.0, 51.0, 52.0, 53.0, 63.0, 65.0, 68.0, 70.0},
		"depth": []float64{50.0, 52.9, 55.9, 57.9, 62.0, 66.0, 71.0, 74.0},
		"length_width": []float64{1.20, 1.24, 1.29, 1.34, 1.50, 1.55, 1.60, 1.65}}
	questions := []string{
		"What is the Table Percentage? ", "What is the Depth Percentage? ",
		"What is the length of diamond? ", "What is the width of diamond? "}

	reader := bufio.NewReader(os.Stdin)
	var input string
	var answer [4]float64
	var err error
	for i, q := range questions {
		for {
                        fmt.Print(q)
			input, _ = reader.ReadString('\n')
			input = strings.TrimSuffix(input, "\n")
			answer[i], err = strconv.ParseFloat(input, 64)
			if err != nil || answer[i] <= 0 || answer[i] >= 100 {
				fmt.Println(inputErrMsg)
				continue
			}
			break
		}
	}
	answer[2] = answer[2]/answer[3]

	fmt.Println("\nScale: Excellent, Very Good, Good, Fair, Poor")

	var scale []float64
	for i, criteria := range referenceKeys{
	// for criteria, scale := range reference {
		for index, value := range reference[criteria] {
			scale = reference[criteria]
			if answer[i] <= value || answer[i] >= scale[8-index-1] {
				fmt.Printf("%s is %s, %g\n", criteria, quality[index], answer[i])
				break
			}
		}
	}
}

func main() {
	OvalQuality()
}

