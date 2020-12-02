

class Solution:
    def find(self, s):
        if not s:
            return 0

        tmp_s = [None] + s
        seen_dict = {}
        dp_swap = [1] * (len(s) + 1)
        dp = [1] * (len(s) + 1)

        for i in range(1, len(tmp_s)):
            if tmp_s[i] in seen_dict:
                seen_dict[tmp_s[i]] += 1
            else:
                seen_dict[tmp_s[i]] = 1

            if tmp_s[i] == tmp_s[i - 1]:
                dp[i] = dp[i - 1] + 1
                dp_swap[i] = dp_swap[i - 1] + 1

            else:
                dp[i] = 1
                # location_dict[tmp_s[i - 1]] = i - 1
                if i - 2 >= 0 and tmp_s[i - 2] == tmp_s[i]:
                    if seen_dict[tmp_s[i]] > dp[i - 2] + 1:
                        dp_swap[i] = dp[i - 2] + 2
                    else:
                        dp_swap[i] = dp[i - 2] + 1

        print(seen_dict)
        print(tmp_s[1:])
        print(dp[1:])
        print(dp_swap[1:])

        return max(dp_swap)


if __name__ == '__main__':
    s = [0, 2, 1, 2, 2, 3, 2, 4, 4, 5]
    print(Solution().find(s))
