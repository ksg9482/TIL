# 해시테이블 기법 사용 -> 수로 변환 -> 배열에 넣으면 인덱스로 접근할 경우 O(1). 인덱스 키는 해시값으로 알 수 있다.
# __getitem__, __setitem__ 은 키 접근 매직 메서드. 이 둘을 실제로 구현해줘야 키로 접근 할 수 있다.
# __len__, __iter__ 내부에서 배열을 이용하기 때문에 배열 매직메서드를 이용할 수 있다.
# __resize__ 배열이 다 차면 확장. 확장 크기는 일정비율로. 파이썬은 ~~을 사용함. 너무 적거나 많지 않은 값. 성능상 이점있다 주장.
# 접근시 완전히 O(1)이 안나오는 이유는 내부적으로 계산을 하고, 해시 충돌로 인해 여러 값이 있을 경우 순회하기 때문 

class MyDict:
    def __init__(self):
        self.size = 16
        self.buckets = [[] for _ in range(self.size)]
        self.length = 0

    def __getitem__(self, key):
        index = hash(key) % self.size
        for k, v in self.buckets[index]:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key, value):
        index = hash(key) % self.size

        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))
        self.length += 1
        if self.length > self.size * 0.6:
            self._resize()

    def __len__(self):
        return self.length

    def __iter__(self):
        for bucket in self.buckets:
            for k, v in bucket:
                yield k

    def items(self):
        for bucket in self.buckets:
            for k, v in bucket:
                yield k, v

    def _resize(self):
        size_change_threshold = 50000
        self.size *= 4 if self.length < size_change_threshold else 2 # 요소 개수에 따라 2, 4. 50000을 기점으로 적으면 4배씩, 많으면 2배씩
        new_buckets = [[] for _ in range(self.size)]
        for bucket in self.buckets:
            for k, v in bucket:
                index = hash(k) % self.size
                new_buckets[index].append((k, v))
        self.buckets = new_buckets


my = MyDict()
my['a'] = 1
my['b'] = 2
my['c'] = 3
print(my.__dict__)

# https://raoneli-coding.tistory.com/m/141
