"""
User enters the Table %, Depth %, length, and width numbers to get rated diamond quality obtained via binary search.

Quality: Excellent, Very Good,              Good,                   Fair,                   Poor
Table%:  53-63,     52 or 64-65,            51 or 66-68,            50 or 69-70,            <50 or >70
Depth%:  58-62,     56-57.9 or 62.1-66,     53-55.9 or 66.1-71,     50-52.9 or 71.1-74,     <50 or >74
Len/Wid: 1.35-1.50, 1.30-1.34 or 1.51-1.55, 1.25-1.29 or 1.56-1.60, 1.20-1.24 or 1.61-1.65, <1.20 or >1.65

Reference: https://www.diamonds.pro/education/oval-cut/
Creator: Kenny Hoang
MIT License
"""
import unittest

# Sorted metric list for each diamond property
POOR, FAIR, GOOD, VERY_GOOD, EXCELLENT = "Poor", "Fair", "Good", "Very Good", "Excellent"
REFERENCE = {
    "table": [
        (POOR, 50.0), (FAIR, 51.0), (GOOD, 52.0), (VERY_GOOD, 53.0), (EXCELLENT, 63.0),
        (VERY_GOOD, 65.0), (GOOD, 68.0), (FAIR, 70.0), (POOR, float("inf"))],
    "depth": [
        (POOR, 50.0), (FAIR, 52.9), (GOOD, 55.9), (VERY_GOOD, 57.9), (EXCELLENT, 62.0),
        (VERY_GOOD, 66.0), (GOOD, 71.0), (FAIR, 74.0), (POOR, float("inf"))],
    "length_width": [
        (POOR, 1.2), (FAIR, 1.24), (GOOD, 1.29), (VERY_GOOD, 1.34), (EXCELLENT, 1.5),
        (VERY_GOOD, 1.55), (GOOD, 1.6), (FAIR, 1.65), (POOR, float("inf"))]
}


def get_rated_quality(metric_list, user_input):
    """
    Do a binary search on a sorted metric list
    """
    length = len(metric_list)
    low, mid, high = 0, length//2, length - 1
    while high - low > 1:
        quality_value = metric_list[mid][1]
        if user_input > quality_value:
            low = mid
            # edge case where a very high value (poor quality)
            # doesn't print because mid will never = high value if
            # mid = ((high - low) // 2) + low
            mid = high - ((high - low) // 2)
        elif user_input < quality_value:
            high = mid
            mid = ((high - low) // 2) + low
        else:
            break
    return metric_list[mid][0]


def get_diamond_quality(answer=None):
    test = True if answer else False

    questions = ("What is the Table Percentage? ", "What is the Depth Percentage? ",
                 "What is the length of diamond? ", "What is the width of diamond? ")

    if not test:
        value = 0
        # get property values
        for q in questions:
            # repeat question for answers <= 0
            while not value or value < 0:
                value = float(input(q))
                answer.append(value)
    # calculate length:width ratio
    answer[2] = answer[2]/answer[3]

    # store values for testing
    ret = []
    if not test: print("\nScale: Excellent, Very Good, Good, Fair, Poor")
    for ans, (diamond_prop, metric_list) in zip(answer[:3], REFERENCE.items()):
        quality_level = get_rated_quality(metric_list, ans)
        if test:
            ret.append(quality_level)
            continue
        print("{} is {}, {}".format(diamond_prop, quality_level, ans))
    return ret


if __name__ == '__main__':
    get_diamond_quality()


class OutputCheck(unittest.TestCase):
    """
    Tests
    """
    def test_get_diamond_quality(self):
        testcases = (
            # cases for very high and low values (outer ends of the scale)
            ([0, 0, 0, 1], [POOR, POOR, POOR]),
            ([100, 100, 1001, 1], [POOR, POOR, POOR],

            # cases for values exactly at a specific metric
            ([50, 50, 1.2, 1], [POOR, POOR, POOR]),
            ([53, 57.9, 1.34, 1], [VERY_GOOD, VERY_GOOD, VERY_GOOD]),
            ([63, 62, 1.5, 1], [EXCELLENT, EXCELLENT, EXCELLENT]))
        )

        for test in testcases:
            self.assertEqual(get_diamond_quality(test[0]), test[1])
