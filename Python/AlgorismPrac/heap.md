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
