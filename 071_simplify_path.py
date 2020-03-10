class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ["/"]
        
        i = 0
        while i < len(path):
            if path[i] == "/":
                if i == len(path) - 1:
                    i += 1
                else:
                    if not ord("a") <= ord(path[i+1]) <= ord("z"):
                        i += 1
                    else:
                        if stack[-1] != "/":
                            stack.append("/")
                        i += 1
            elif path[i] == ".":
                if i == len(path) - 1:
                    i += 1
                else:
                    if path[i+1] == ".":
                        tmp = stack.pop()
                        while tmp != "/" and len(stack) != 0:
                            tmp = stack.pop()
                        if len(stack) == 0:
                            stack.append("/")
                        i += 2
                    else:
                        i += 1
            else:
                stack.append(path[i])
                i += 1
        
        return "".join(x for x in stack)


if __name__ == "__main__":
    a = Solution()
    print(a.simplifyPath("/a//b////c/d//././/.."))