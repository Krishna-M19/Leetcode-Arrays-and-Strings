class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "X": 10, "V":5, "L":50, "C": 100, "D":500, "M":1000}
        summ = 0
        n = len(s)
        i = 0

        while i < n:
            if i < n-1 and d[s[i]] < d[s[i+1]]:
                summ += d[s[i+1]]-d[s[i]]
                i += 2

            else:
                summ += d[s[i]]

        return 
    

#optimal solution
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'M': 1000}

        total = 0
        prev_value = 0

        # Iterate through the string from right to left
        for char in reversed(s):
            current_value = roman_to_int[char]

            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            prev_value = current_value

        return total


# Testing
s = Solution()
print(s.romanToInt("MXCDIV"))
