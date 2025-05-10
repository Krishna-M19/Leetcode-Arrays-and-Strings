class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = 0, 0
        s = []

        word = 1
        while a<len(word1) and b<len(word2):
            if word == 1:
                s.append(word1[a])
                a+=1
                word = 2
            else:
                s.append(word2[b])
                b+=1
                word = 1
        
        while a<len(word1):
            s.append(word1[a])
            a+=1
        while b<len(word2):
            s.append(word2[b])
            b+=1

        return "".join(s)
    
print(Solution().mergeAlternately("AIRLINE", "PKN"))