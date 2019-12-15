class Solution:
    def permute(self, nums):
        self.rst = []
        self.find([], nums)
        return self.rst
        
    def find(self, combo, rest):
        if len(rest) == 0:
            self.rst.append(combo)
        for i in range(len(rest)):
            self.find(combo + [rest[i]], rest[:i] + rest[i+1:])

if __name__ == "__main__":
    a = Solution()
    b = [1,2,3]
    print(a.permute(b))