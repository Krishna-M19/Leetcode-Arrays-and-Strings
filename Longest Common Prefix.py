from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')

        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        
        return strs[:i]
print(Solution().longestCommonPrefix(["flower","flow","flight"]))



#optimal Solution:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        strs = sorted(strs)
        f, l = strs[0], strs[-1]
        for i in range(len(f)):
            if i<len(l) and f[i] == l[i]:
                result += f[i]
            else:
                return result
        return result