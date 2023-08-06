"""
At the end of the first year there will be:
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be:
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

More generally given parameters:

p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)

the function nb_year should return n number of entire years needed to get a population greater or equal to p.

aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)
"""


def nb_year(p0, percent, aug, p):
    year_counter = 1
    while (p0 := (p0 * (1 + percent / 100) + aug) // 1) < p:
        year_counter += 1
    return year_counter

    # через рекурсию
    # t = 0
    # while p0 < p:
    #     p0 = int(p0*(1 + percent/100)) + aug  # my mathematical brain hates that I need to round this
    #     t += 1
    # return t


print(nb_year(1000, 2.0, 50, 1214))
