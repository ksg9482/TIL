class myCircularQueue:
    def __init__(self, k:int):
        self.q = [None] * k
        self.maxlen = k
        # 두개 포인터는 각각 큐의 시작과 끝
        self.p1 = 0
        self.p2 = 0

    #rear포인터 이동
    def en_queue(self, value:int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    #front포인터 이동
    def de_queue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True
    
    def front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]
    
    def rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def is_enpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None
    
    def is_full(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None
