"""
User enters the Table %, Depth %, length, and width numbers
to get diamond quality.

Quality: Excellent, Very Good,              Good,                   Fair,                   Poor
Table%:  53-63,     52 or 64-65,            51 or 66-68,            50 or 69-70,            <50 or >70
Depth%:  58-62,     56-57.9 or 62.1-66,     53-55.9 or 66.1-71,     50-52.9 or 71.1-74,     <50 or >74
Len/Wid: 1.35-1.50, 1.30-1.34 or 1.51-1.55, 1.25-1.29 or 1.56-1.60, 1.20-1.24 or 1.61-1.65, <1.20 or >1.65

Reference: https://www.diamonds.pro/education/oval-cut/
Creator: Kenny Hoang
MIT License
"""

import math
import pytest
from datetime import datetime


def main(answer=[]):
    start_time = datetime.now()
    quality = ["Poor", "Fair", "Good", "Very Good", "Excellent"]
    reference = {
        "table": [
            50.0, 51.0, 52.0, 53.0, 63.0, 65.0, 68.0, 70.0
        ],
        "depth": [
            50.0, 52.9, 55.9, 57.9, 62.0, 66.0, 71.0, 74.0
        ],
        "length_width": [
            1.20, 1.24, 1.29, 1.34, 1.50, 1.55, 1.60, 1.65
        ]
    }
    questions = ("What is the Table Percentage? ", "What is the Depth Percentage? ",
                 "What is the length of diamond? ", "What is the width of diamond? ")

    if not answer:
        for q in questions:
            while True:
                try:
                    value = float(input(q))
                    assert value or math.sqrt(value) < 10.0
                    answer.append(value)
                    break
                except (AssertionError, ValueError):
                    print("Please enter a number between 0 and 100")

    answer[2] = answer[2]/answer[3]

    print("\nScale: Excellent, Very Good, Good, Fair, Poor")

    for i, (criteria, scale) in zip(range(3), reference.items()):
        for index, value in enumerate(scale):
            if answer[i] <= value or answer[i] >= scale[8-index-1]:
                print("{} is {}, {}".format(criteria, quality[index], answer[i]))
                break

    print("Execution time:", datetime.now()-start_time)


if __name__ == '__main__':
    main()


@pytest.mark.repeat(10)
def test_main():
    start = datetime.now()
    values = [25, 25, 1.1, 1]
    main(values)
    print("time:", datetime.now()-start)
