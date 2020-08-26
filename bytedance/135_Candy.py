class Solution:
    def candy(self, ratings):
        candidates = [1] * len(ratings)

        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                candidates[i+1] = candidates[i] + 1
        
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i] and candidates[i-1] <= candidates[i]:
                candidates[i-1] = candidates[i] + 1

        return sum(candidates)

print(Solution().candy([1, 0, 2]))