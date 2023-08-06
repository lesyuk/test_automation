"""
For this problem you must create a program that says who ate the last cookie. If the input is a string then "Zach" ate
the cookie. If the input is a float or an int then "Monica" ate the cookie. If the input is anything else "the dog" ate
the cookie. The way to return the statement is: "Who ate the last cookie? It was (name)!"
"""


def cookie(x):
    string = "Who ate the last cookie? It was {}!"
    if type(x) is str:
        return string.format('Zach')
    return string.format('Monica') if type(x) in (int, float) else string.format('the dog')

    # another solution
    # return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")
