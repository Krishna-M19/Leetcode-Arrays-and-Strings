class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in t:
            if i < len(s) and s[i] == j:
                i += 1
        return i == len(s)
    

# Soln with regex

import re
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pattern = ".*".join(map(re.escape, s))

        return bool(re.search(pattern, t)) is not None