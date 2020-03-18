class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []

        for word in s.split(" "):
            if not word:
                continue
            if stack:
              stack.append(" ")
            stack.append(word)

        rst = ""
        while stack:
            rst += stack.pop()

        return rst  