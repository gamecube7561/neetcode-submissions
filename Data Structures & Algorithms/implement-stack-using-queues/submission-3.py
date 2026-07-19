class MyStack:

    def __init__(self):
        self.stack1 = deque()
        self.top_val = -1

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.top_val = x
        

    def pop(self) -> int:
        ret = self.stack1.pop()
        if len(self.stack1) > 0:
            self.top_val = self.stack1[-1]
        return ret

    def top(self) -> int:
        return self.top_val

    def empty(self) -> bool:
        if len(self.stack1) >= 1:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()