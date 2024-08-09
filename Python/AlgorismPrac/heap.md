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
