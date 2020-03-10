class Solution:
    def search(self, nums, target):
        self.nums = nums
        self.target = target
        return self.search(0, len(nums)-1)
    
    def search(self, l, r):
        if l > r:
            return -1
        else:
            m = floor((l + r)/2)
            if nums[m] == self.target:
                return m
            elif self.nums[m] > self.target:
                return self.search(l, m)
            else:
                return self.search(m+1, r)

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            target = int(line);
            
            ret = Solution().search(nums, target)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()