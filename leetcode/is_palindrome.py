def is_palindrome(x: int) -> bool:
    if x < 0 or not x % 10 and x:
        return False

    reverted_x = 0
    while x > reverted_x:
        reverted_x = reverted_x * 10 + (x % 10)
        x //= 10

    return x == reverted_x or x == reverted_x // 10


print(is_palindrome(1221))
print(is_palindrome(-100))
print(is_palindrome(0))
print(is_palindrome(123421))
