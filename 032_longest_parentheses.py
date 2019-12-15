class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        length = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    new_length = i - stack[-1]
                    if new_length > length:
                        length = new_length
        return length

def main():
            s = ")()())"
            
            ret = Solution().longestValidParentheses(s)

            out = str(ret)
            print(out)


if __name__ == '__main__':
    main()

