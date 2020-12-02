class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []

        for item in tokens:
            if item.isdigit() or item[1:].isdigit():
                stack.append(int(item))
                continue

            num2 = stack.pop()
            num1 = stack.pop()

            if item == '+':
                stack.append(num1 + num2)

            elif item == '-':
                stack.append(num1 - num2)

            elif item == '*':
                stack.append(num1 * num2)

            elif item == '/':
                stack.append(int(num1 / num2))

        return stack[-1]


if __name__ == '__main__':
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
