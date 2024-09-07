
김석규
오후 6:22 (3시간 전)
나에게

https://leetcode.com/problems/add-digits/description/?envType=problem-list-v2&envId=simulation&difficulty=EASY

숫자 각 자리를 별개 숫자로 인식해서 더하는 문제

한자리 수가 되면 반환 한다

33ms. Beats 76.68%

16.53MB. Beats 32.03%

O(n^2). 다중 반복문

```python
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = [int(digit) for digit in str(num)]
            num = sum(num)

        return num
```
---

https://leetcode.com/problems/fizz-buzz/?envType=problem-list-v2&envId=simulation&difficulty=EASY

숫자 맞춰서 특정 문자열을 리스트에 섞는 문제.

3으로 나눠진다, 5로 나눠진다, 3과 5 전부 나눠진다

처리하는 함수 만들고 리스트 컴프리헨션으로 하면 될 듯

43ms. Beats 53.92%

17.72MB. Beats 7.43%

O(n)

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [self.fizzBuzz_checker(data) for data in range(1, n + 1)]
       
        return ans

    def fizzBuzz_checker(self, digit):
        if digit % 15 == 0:
            return "FizzBuzz"
        elif digit % 3 == 0:
            return "Fizz"
        elif digit % 5 == 0:
            return "Buzz"
        else:
            return str(digit)
```
---

https://leetcode.com/problems/add-strings/description/?envType=problem-list-v2&envId=simulation&difficulty=EASY

굳이 전부 숫자로 바꿔놓지 않아도 됨. 몫과 나머지 구해서 넣는 방식으로 처리한다.

int로 직접 바꾸지 말라고 되어있긴 한데 실제로 않쓰면 성능이 지나치게 낮게 나왔다.

이 때는 {문자열:숫자} 사전을 만들고 자릿수를 곱해서 숫자를 만드는 방식을 사용했다.

35ms. Beats 88.92%

17.00MB. Beats 35.89%

O(n)

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == "0":
            return num2
        if num2 == "0":
            return num1
        
        result = []
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        
        while i >= 0 or j >= 0 or carry:
            digit_sum = carry
            
            if i >= 0:
                digit_sum += int(num1[i])
                i -= 1
            if j >= 0:
                digit_sum += int(num2[j])
                j -= 1
            
            result.append(str(digit_sum % 10))
            carry = digit_sum // 10
        
        return ''.join(result[::-1])
```
---
"""
https://leetcode.com/problems/available-captures-for-rook/description/?envType=problem-list-v2&envId=simulation&difficulty=EASY

룩이 잡을 수 있는 폰 갯수를 세는 문제. 2차원 배열. 중간에 막히면 못잡음.

룩 위치 제공 안됨 -> 순회로 찾아야 함. 

어차피 찾을 거 다 찾은 후 계산하자

33ms. Beats 81.96%

16.62MB. Beats 6.01%

O(1). 타겟이 많아도 결국 1개씩 잡으면 종료됨. 입력의 크기 자체는 항상 고정.
"""

```python
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        unit_to_point_dict = defaultdict(str)
        start = []
        ans = 0
        for r_idx, row in enumerate(board):
            for c_idx, col in enumerate(row):
                if col == "R":
                    start = [r_idx, c_idx]
                if not col == ".":
                    unit_to_point_dict[f'{[r_idx, c_idx]}'] = col

        # up
        for i in range(start[0] - 1, -1, -1):
            point = unit_to_point_dict.get(f'{[i, start[1]]}')
            if point and point == "p":
                ans += 1
                break
            elif point and not point == "p":
                break

        # down
        for i in range(start[0] + 1, 9):
            point = unit_to_point_dict.get(f'{[i, start[1]]}')
            if point and point == "p":
                ans += 1
                break
            elif point and not point == "p":
                break
        
        # left
        for i in range(start[1] - 1, -1, -1):
            point = unit_to_point_dict.get(f'{[start[0], i]}')
            if point and point == "p":
                ans += 1
                break
            elif point and not point == "p":
                break
        
        # right
        for i in range(start[1] + 1, 9):
            point = unit_to_point_dict.get(f'{[start[0], i]}')
            if point and point == "p":
                ans += 1
                break
            elif point and not point == "p":
                break

        return ans
```
---

https://leetcode.com/problems/teemo-attacking/description/?envType=problem-list-v2&envId=simulation&difficulty=EASY

초당 1씩 가산 -> 현재 - 과거 해서 작은걸로 넣는다. 

시간이 더 커도 duration 이상으론 안 들어간다.

194ms. Beats 56.35%

17.90MB. Beats 95.07%

O(n)

```python
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0

        for i in range(len(timeSeries) - 1):
            poisoned_time = min(duration, timeSeries[i+1]-timeSeries[i])
            ans += poisoned_time

        ans += duration
        
        return ans
```
---

https://leetcode.com/problems/reshape-the-matrix/?envType=problem-list-v2&envId=simulation&difficulty=EASY

n차원 배열을 m차원 배열로 변환하는 문제

숫자 갯수가 맞는지 확인

맞으면 변환 아니면 원본 반환

모듈러 연산으로 인덱스 관리

75ms. Beats 60.98%

17.12MB. Beats 97.72%

O(n)

```python
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row_len = len(mat)
        col_len = len(mat[0])
        ans = [[] for _ in range(r)]

        if not (col_len * row_len) == r * c:
            return mat
        
        count = 0
        idx = 0
        for row in mat:
            for col in row:
                ans[idx].append(col)
                count += 1
                if count % c == 0:
                    idx += 1

        return ans
```
---
