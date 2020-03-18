# maintain a min
# solution: push min when a new min comes
# if new <= min: push, push
# else: push


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mn = float("inf")


    def push(self, x: int) -> None:
        if x <= self.mn:
            self.stack.append(self.mn)
            self.mn = x
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.mn:
            self.mn = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mn