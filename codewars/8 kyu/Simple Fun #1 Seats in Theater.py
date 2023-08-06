"""
Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column you're
 sitting in, return the number of people who sit strictly behind you and in your column or to the left, assuming all
 seats are occupied.
"""


def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - col + 1) * (tot_rows - row)


print(seats_in_theater(16,11,5,3))