class MyStack:

    def __init__(self):
        import queue
        self.q = queue.Queue()

    def push(self, x: int) -> None:
        self.q.put(x)
        for i in range(1, self.q.qsize()):
            self.q.put(self.q.get())

    def pop(self) -> int:
        return self.q.get()
        

    def top(self) -> int:
        return self.q.queue[0]

    def empty(self) -> bool:
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()