class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
             'CM': 900, 'M': 1000}
        new_integer = 0
        i = 0
        while i < len(s):
            if d[s[i]] >= d[s[i - (len(s) - 1)]] or i == len(s) - 1:
                new_integer += d[s[i]]
                i += 1
            else:
                new_integer += d[s[i] + s[i - (len(s) - 1)]]
                i += 2

        return new_integer


sol = Solution()
print(sol.romanToInt('LVIII'))