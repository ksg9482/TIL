# 스택을 이용한 큐 구현

# 스택 2개 이용
class myQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x): #요소 x를 큐 마지막에 삽입.
        self.input.append(x)
    
    def pop(self): #큐 처음에 있는 요소를 제거
        self.peek()
        return self.output.pop()
    
    def peek(self): #큐 처음에 있는 요소 조회
        #output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    
    def empty(self): #큐가 비어있는지 반환.
        return self.input == [] and self.output == []

# 맨 뒤의 아이템을 끄집어 낼 수 밖에 없다. 스택의 연산만을 이용해서 풀기 위해선 2개의 스택이 필요하다.
