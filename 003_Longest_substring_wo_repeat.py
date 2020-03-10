class Solution:
    def lengthOfLongestSubstring(self, s):
        ls = list(s)
        if not ls:
            return 0
        p1 = p2 = 0
        mx = 1
        while p1 < len(ls):
            seen = {}
            seen[ls[p1]] = p1
            p2 = p1 + 1
            while p2 < len(ls):
                if ls[p2] not in seen:
                    if p2 - p1 + 1 > mx:
                        mx = p2 - p1 + 1
                    seen[ls[p2]] = p2
                    p2 += 1 
                else:
                    p2 = seen[ls[p2]] + 1
                    break
            p1 = p2
                
        
        return mx

print(Solution().lengthOfLongestSubstring("dvdff"))