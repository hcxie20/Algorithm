class Solution:
    def longestConsecutive(self, nums) -> int:
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            if not num - 1 in num_set:
                current_num = num
                length = 1

                while current_num + 1 in num_set:
                    length += 1
                    current_num += 1
                if length > max_length:
                    max_length = length

        return max_length