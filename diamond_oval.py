"""User enters the Table %, Depth %, length, and width numbers
to get diamond quality based on https://www.diamonds.pro/education/oval-cut/
Creator: Kenny Hoang
MIT License
"""

import math

"""Table% are (from Excellent to Poor): 
    53-63, 52 or 64-65, 51 or 66-68, 50 or 69-70, <50 or >70
    """
table_reference = {
    "Excellent": [[53.0, 10.0]],
    "Very Good": [[52.0,  1.0], [63.0,  2.0]],
         "Good": [[51.0,  1.0], [65.0,  3.0]],
         "Fair": [[50.0,  1.0], [68.0,  2.0]],
         "Poor": [[00.0, 50.0], [70.0, 30.0]]
}

"""Depth %	are (from Excellent to Poor):
    58-62, 56-57.9 or 62.1-66, 53-55.9 or 66.1-71, 50-52.9 or 71.1-74, <50 or >74
    """
depth_reference = {
    "Excellent": [[58.0, 4.0]],
    "Very Good": [[56.0, 2.0], [62.0, 4.0]],
         "Good": [[53.0, 3.0], [66.0, 5.0]],
         "Fair": [[50.0, 3.0], [71.0, 3.0]],
         "Poor": [[0.0, 50.0], [74.0, 26.0]]
}

"""Length/Width Ratios	are (from Excellent to Poor):
    1.35-1.50, 1.30-1.34 or 1.51-1.55, 1.25-1.29 or 1.56-1.60, 1.20-1.24 or 1.61-1.65, <1.20 or >1.65
    """
length_width_reference = {
    "Excellent": [[1.35, 0.15]],
    "Very Good": [[1.30, 0.05], [1.50, 0.05]],
         "Good": [[1.25, 0.05], [1.55, 0.05]],
         "Fair": [[1.20, 0.05], [1.60, 0.05]],
         "Poor": [[0.00, 1.20], [1.65, 100.0]]
}


def main():
    questions = ["What is the Table Percentage? ", "What is the Depth Percentage? ", "What is the length of diamond? ", "What is the width of diamond? "]
    str_diamond_prop = ["Table %", "Depth % ", "Length/Width ratio"]
    diamond_prop = [table_reference, depth_reference, length_width_reference]
    buy_prop = [0.0, 0.0, 0.0, 0.0]

    value_assigned, q = False, 0

    while value_assigned is False:
        while q < 4:
            try:
                buy_prop[q] = float(input(questions[q]))
                assert math.sqrt(buy_prop[q]) < 10.0
                q += 1
            except(AssertionError, ValueError):
                print("Please enter a number between 0 and 100")

        buy_prop[2] = buy_prop[2]/buy_prop[3]
        value_assigned = True

    print("\nScale: Excellent, Very Good, Good, Fair, Poor")

    for p in range(3):
        match = False
        for quality, ranges in diamond_prop[p].items():
            for value in ranges:
                if buy_prop[p] >= value[0] and buy_prop[p] <= (value[0]+value[1]):
                    print("{} is {}, {}".format(str_diamond_prop[p], quality, buy_prop[p]))
                    match = True

            if match is True:
                break
    
    # Formatting purposes at the end of output
    print("")


if __name__ == '__main__':
    main()

