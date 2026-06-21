class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dq = deque()
        for t in tokens:
            if t == "+":
                t1 = dq.pop()
                t2 = dq.pop()
                dq.append(int(t1)+int(t2))
            elif t == "*":
                t1 = dq.pop()
                t2 = dq.pop()
                dq.append(int(t1)*int(t2))
            elif t == "-":
                t1 = dq.pop()
                t2 = dq.pop()
                dq.append(int(t2)-int(t1))
            elif t == "/":
                t1 = dq.pop()
                t2 = dq.pop()
                dq.append(int(float(t2)/t1))
            else:
                dq.append(int(t))
            print(dq)
        return int(dq.pop())