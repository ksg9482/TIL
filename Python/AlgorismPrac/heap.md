https://leetcode.com/problems/minimum-number-game/description/

최소힙을 사용하는 문제

두명이 각각 하나씩 최소값을 뽑고, 각각 역순으로 결과배열에 넣는다 

47ms. Beats 86.29%

16.72MB. Beats 5.15%

O(n)

```python
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        ans = []
        temp = []
        while range(len(nums)):
            min_num = heapq.heappop(nums)
            temp.append(min_num)

            if len(temp) >= 2:
                ans.extend([temp[1], temp[0]])
                temp = []

        return ans
```
---

https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/

가장 큰 요소 2개를 선택하는 문제

heap을 이용해서 가장 큰 2개를 고른다.

i-1, j-1 해서 곱한다

47ms. Beats 80.54%

16.75MB. Beats 5.68%

O(nlogn). 힙만들어야 한다

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        max_heap = []
        # max heap으로 사용하기 위해 부호 변경
        for num in nums:
            heapq.heappush(max_heap, -num)

        for _ in range(2):
            max_num = -heapq.heappop(max_heap)
            if not ans:
                ans += (max_num - 1)
            else:
                ans *= (max_num - 1)
        return ans
```
---
https://leetcode.com/problems/delete-greatest-value-in-each-row/description/

다중배열을 최대힙으로 만들어서 가장 큰 수 제거

가장 큰 수 끼리 비교해서 최대값에 합산한다.

81ms Beats 89.79%

16.84MB Beats 10.95%

O(n * m). n * m 사각형 처리

```python
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        max_heap_grid = []
        ans = 0
        for grid_items in grid:
            max_heaps = []
            for item in grid_items:
                heapq.heappush(max_heaps, -item)
            max_heap_grid.append(max_heaps)
        
        for _ in range(len(max_heap_grid[0])):
            max_items = []
            for grid_items in max_heap_grid:
                max_items.append(-heapq.heappop(grid_items))
            ans += max(max_items)
        
        return ans
```
---

https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/

각 배열에서 1의 개수를 구하고 배열 만들기.

그 배열에는 인덱스, 우선순위 들어있음

인덱스 리스트를 반환하되, 값이 같으면 우선순위로 판단

95ms. Beats 57.08%

16.84MB. Beats 66.99%

O(nlogn)

```python
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sum_list = []
        ans = []
        for idx, rows in enumerate(mat):
            sum_list.append((sum(rows), idx))
        heapq.heapify(sum_list)
        for _ in range(k):
            ans.append(heapq.heappop(sum_list)[1])
        return ans
```
---

https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

리스트에서 최소값 찾기. 최소값과 동일한 값을 0으로 만들고 리스트가 0만 있을때까지 반복.

총 반복이 몇번 필요한가.

최소힙으로 찾으면서 카운트

35ms. Beats 77.27%

16.54MB. Beats 32.02%

O(nlogn)

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min_heap = []
        ans = 0
        for num in nums:
            heapq.heappush(min_heap, num)

        prev_num = 0
        for _ in range(len(min_heap)):
            heap_item = heapq.heappop(min_heap)
            if heap_item == prev_num:
                pass
            else:
                ans += 1
                prev_num = heap_item

        return ans
```
---

https://leetcode.com/problems/relative-ranks/description/

리스트에 스코어에 맞춰 금,은,동으로 바꾸는 문제

최대힙에 스코어와 인덱스를 넣는다

최대힙 3개로 인덱스에 맞춰 금,은,동으로 변환

65ms. Beats 57.56%

18.02MB. Beats 10.62%

O(nlogn)

```python
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        max_heap = []
        for idx, item in enumerate(score):
            heapq.heappush(max_heap, (-item, idx))
        
        medal_list = [
            "Gold Medal",
            "Silver Medal",
            "Bronze Medal"
        ]
        for i in range(len(score)):
            heap_item = heapq.heappop(max_heap)
            grade = medal_list[i] if len(medal_list) > i else str(i + 1) # 1등부터 시작
            score[heap_item[1]] = grade

        return score
```
---

https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/

선물리스트의 k번째 까지의 아이템을 제곱근으로 바꾸는 합산하는 문제

최대를 구하는 건 최대힙 이용

제곱근 구해서 최대힙에 넣어 비교.

기존 최대가 아니라 제곱근 처리한 값도 넣어서 같이 비교해야 함

44ms. Beats 87.53%

16.78MB. Beats 28.38%

O(nlogn)

```python
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = []
        for gift in gifts:
            heapq.heappush(max_heap, -gift)

        for _ in range(k):
            heap_item = heapq.heappop(max_heap)
            heapq.heappush(max_heap, -int(math.sqrt(-heap_item)))

        return -sum(max_heap)
```
---

https://leetcode.com/problems/last-stone-weight/description/

돌 하나만 남기고 제거하는 문제

최대힙으로 2개씩 고른다

i, j 비교해서 다르면 i - j, 같으면 둘다 제거

22ms. Beats 99.53%

16.43MB. Beats 70.48%

O(nlogn)

```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            
            temp = []
            for _ in range(2):
                heap_item = -heapq.heappop(max_heap)
                temp.append(heap_item)
            diff = temp[0] - temp[1]

            if diff == 0:
                pass
            else:
                heapq.heappush(max_heap, -diff)
        
        if len(max_heap) == 0:
            return 0
        
        return -max_heap[0]
```
---
