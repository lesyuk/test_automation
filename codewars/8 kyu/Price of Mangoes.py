"""
There's a "3 for 2" (or "2+1" if you like) offer on mangoes. For a given quantity and price (per mango),
calculate the total cost of the mangoes.
"""


def mango(quantity, price):
    return (quantity - quantity // 3) * price


print(mango(3, 3))
