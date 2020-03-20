class CQueue:
    # 可以利用一个栈进行放元素，然后把这个栈里面的元素弹出移到另外一个栈

    def __init__(self):
        self.stackA = []
        self.stackB = []

    def appendTail(self, value: int) -> None:
        self.stackA.append(value)

    def deleteHead(self) -> int:
        if len(self.stackA) == 0 and len(self.stackB) == 0:
            return -1
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()
        else:
            return self.stackB.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()