class Solution:
    def permuteUnique(self, nums):
        self.rst = []
        print(nums.sort())
        self.find([], nums.sort())
        return self.rst
        
    def find(self, combo, rest):
        if len(rest) == 0:
            self.rst.append(combo)
        i = 0
        while i < (len(rest)):
            while i < len(rest)-2 and rest[i] == rest[i+1]:
                i += 1
            self.find(combo + [rest[i]], rest[:i] + rest[i+1:])
            i += 1

if __name__ == "__main__":
    a = [1, 1, 2]
    b = Solution()
    print(b.permuteUnique(a))