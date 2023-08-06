"""
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!
"""


def better_than_average(class_points, your_points):
    return sum(class_points) / len(class_points) < your_points


print(better_than_average([2, 3], 5))
