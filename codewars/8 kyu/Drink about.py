"""
Kids drink toddy.
Teens drink coke.
Young adults drink beer.
Adults drink whisky.
Make a function that receive age, and return what they drink.
"""


def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    elif age < 18:
        return 'drink coke'
    elif age < 21:
        return 'drink beer'
    return 'drink whisky'


# d = {range(0, 14): 'drink toddy',
#      range(14, 18): 'drink coke',
#      range(18, 21): 'drink beer',
#      range(18): ''}

print(people_with_age_drink(13))
