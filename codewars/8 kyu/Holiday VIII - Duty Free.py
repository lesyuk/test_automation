"""
You will be given the high street price (normPrice, in £ (Pounds)),
the duty free discount (discount, in percent) and the cost of the holiday (in £).

For example, if a bottle costs £10 normally and the duty free discount is 10%, you would save £1 per bottle. If your
holiday will cost £500, you would have to purchase 500 bottles to save £500, so the answer you return should be 500.
"""


def duty_free(price, discount, holiday_cost):
    # return int(holiday_cost / (price / 100 * discount))

    # another solution
    return holiday_cost // (price * (discount / 100))


print(duty_free(17, 10, 500))