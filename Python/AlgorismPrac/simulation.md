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

https://leetcode.com/problems/robot-return-to-origin/description/?envType=problem-list-v2&envId=simulation&difficulty=EASY

포인트의 좌표 이동이 끝났을 때 원점으로 돌아오나 확인하는 문제

ud, lr 한 쌍 개수가 맞으면 원점으로 돌아온다.

계산 마치고 둘다 0이면 원점.

46ms. Beats 73.02%

16.54MB. Beats 53.14%

O(n)

```python
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u_count = 0
        l_count = 0

        for move in moves:
            if move == "U":
                u_count += 1
            elif move == "D":
                u_count -= 1
            elif move == "L":
                l_count += 1
            else:
                l_count -= 1
        
        return u_count == 0 and l_count == 0
```
---

https://leetcode.com/problems/transpose-matrix/?envType=problem-list-v2&envId=simulation&difficulty=EASY

2차원 리스트 축을 90도 돌리는 문제

데크에 값 넣고 마지막에 리스트로 변환한다.

60ms. Beats 87.49%

17.46MB. Beats 12.24%

O(n*m) col과 row가 클수록 오래걸림

```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        col_len = len(matrix[0])
        ans = deque([deque() for _ in range(col_len)])

        for row in matrix:
            for idx, col in enumerate(row):
                target_idx = idx % col_len
                ans[target_idx].append(col)

        for i in range(len(ans)):
            ans[i] = list(ans[i])
        
        return list(ans)
```
---
https://leetcode.com/problems/distribute-candies-to-people/description/?envType=problem-list-v2&envId=simulation&difficulty=EASY

사탕을 순서대로 분배하는 문제.

숫자에 맞게 분배 할 수 없을 때, 남은 사탕은 다 줌.

리스트에 순서에 맞게 가산하여 처리.

35ms. Beats 82.96%

16.72MB. Beats 6.02%

O(n). candies가 클수록 연산 횟수 많아짐

```python
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = deque([0 for _ in range(num_people)])
        count = 0
        idx = 0
        candy = 1

        while candy <= candies:
            modulo_idx = idx % num_people
            count += candy
            candies -= candy
            ans[modulo_idx] += candy
            candy += 1
            idx += 1
        
        ans[idx % num_people] += candies

        return list(ans)
```
---

https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description/?envType=problem-list-v2&envId=simulation&difficulty=EASY

매트릭스의 특정 포인트 기준으로 십자에 값 더하는 문제

실제로 만들고 연산한다.

나중에 홀수 몇개인지 찾는다

40ms. Beats 84.64%

16.51MB. Beats 79.62%

O(n*m)

```python
class Solution:
    
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        matrix = [[0 for i in range(m)] for j in range(n)] 
        
        def inc(x, y):
            
            for i in range(m):
                matrix[x][i] += 1
            
            for i in range(n):
                matrix[i][y] += 1
                
        for ind in indices:
            inc(ind[0], ind[1])
            
            
        return sum([0 if n % 2 == 0 else 1 for l in matrix for n in l])
```
---
https://leetcode.com/problems/calculate-amount-paid-in-taxes/description/?envType=problem-list-v2&envId=simulation&difficulty=EASY

세금 내역을 누적해서 계산하는 문제

세금 계산 조건이 언제 바뀌는지 파악해야 한다.

income 보다 커질 때 조건 바뀜

67ms. Beats 81.96%

16.65MB. Beats 35.75%

O(n)

```python
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0
        prev = 0
        for bracket in brackets:
            
            if bracket[0] > income:
                ans += (income - prev) * (bracket[1] / 100)
                break
            else:
                ans += (bracket[0] - prev) * (bracket[1] / 100)
                prev = bracket[0]

        return ans
```
---

https://leetcode.com/problems/shift-2d-grid/?envType=problem-list-v2&envId=simulation&difficulty=EASY

순서대로 처리한다. 

처리속도를 위해서 삽입할 데크를 미리 만들어둔다.

한 칸씩 뒤로 밀고 맨 뒤는 맨 앞으로.

맨 앞은 col 조작이 한 번 더 들어간다.

126ms. Beats 57.44%

16.96MB. Beats 57.44%

```python
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        grid_deque = deque()

        for row in grid:
            grid_deque.append(deque(row))
        for i in range(k):
            for row_deque in grid_deque:
                poped = row_deque.pop()
                row_deque.appendleft(poped)
            else:
                last_num = grid_deque[-1][0]
                for i in range(len(grid_deque)):
                    last_num, grid_deque[i][0] = grid_deque[i][0], last_num
        for i in range(len(grid_deque)):
            grid_deque[i] = list(grid_deque[i])
           
        return list(grid_deque)
```
---

https://leetcode.com/problems/create-target-array-in-the-given-order/description/?envType=problem-list-v2&envId=simulation&difficulty=EASY

요소를 삽입하며 리스트 만드는 문제.

단순히 삽입으로 처리해도 될 듯 하다. 데크에 넣자.

33ms. Beats 82.02%

16.36MB. Beats 93.63%

O(n)

```python
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = deque()
        for num, idx in zip(nums, index):
            ans.insert(idx, num)
        return list(ans)
```
---

https://leetcode.com/problems/water-bottles/?envType=problem-list-v2&envId=simulation&difficulty=EASY

물병을 더 교환할 수 없을 때까지 합산하는 문제

마시기 -> numExchange 만큼 비율 교환 -> 마시기 반복.

빈병 교환비율 안될 시 반복 종료

34ms. Beats 59.39%

16.53MB. Beats 35.10%

O(logn). 반복마다 numExchange씩 작아짐 

```python
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles

        while empty >= numExchange:
            changed = empty // numExchange
            ans += changed
            empty = empty - (numExchange * changed)
            empty += changed
        
        return ans
```
---
