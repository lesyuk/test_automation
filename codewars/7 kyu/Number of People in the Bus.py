"""
There is a bus moving in the city which takes and drops some people at each bus stop.

You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get
on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.

Your task is to return the number of people who are still on the bus after the last bus stop (after the last array).
"""
from functools import reduce


def number(bus_stops):
    return sum(get - get_off for get, get_off in bus_stops)


print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
