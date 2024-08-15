https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

음수 개수를 구하는 문제. 

이진검색 문제로 접근하면 플랫하게 정렬 -> 음수에서 양수로 넘어가는 구간 찾기

그 구간의 인덱스 바로 전은 다 음수

98ms. Beats 82.95%

17.98MB. Beats 20.41%

O(nlogn)

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        num_list = []
        for items in grid:
            num_list.extend(items)
        num_list.sort()
        start = 0 
        end = len(num_list) - 1

        if len(num_list) == 1:
            return len(num_list) if num_list[0] < 0 else 0
        
        while start <= end:
            mid = math.ceil((start + end) / 2)
            current_item = num_list[mid]
            prev_item = num_list[mid - 1]
            if (current_item >= 0) and (prev_item < 0):
                return mid 
            elif prev_item >= 0:
                end = mid - 1
            else:
                start = mid + 1

        return mid
```
---

https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

정렬 후 target과 같은 요소의 인덱스 리스트를 구하는 문제

이진검색으로 요소 찾고 투포인터로 +-1씩 인덱스 바꿔서 집계

이진검색 말고 정렬 -> 일반 집계로 바로 하는게 더 좋을듯 하나

47ms. Beats 61.53%

16.57MB. Beats 30.59%

O(nlogn)

```python
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        start = 0 
        end = len(nums) - 1

        while start <= end:
            mid = math.ceil((start + end) / 2)
            if nums[mid] == target:
                inner_left = mid - 1
                inner_right = mid + 1
                ans.append(mid)
                if inner_left >= 0:
                    while nums[inner_left] == target:
                        ans.append(inner_left)
                        inner_left -= 1
                        if inner_left < 0:
                            break
                if inner_right <= len(nums) - 1:
                    while nums[inner_right] == target:
                        ans.append(inner_right)
                        inner_right += 1
                        if inner_right > len(nums) - 1:
                            break
                break 
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        ans.sort()
        return ans
```
---
https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/

음수 개수, 양수 개수 중 최대 개수를 반환하는 문제

음수 구하고 양수 구해서 max

괜히 동시에 하려고 힘빼지 말고 따로 따로 해도 충분한 시간복잡도 나온다

102ms. Beats 77.72%

16.84MB. Beats 53.78%

O(logn)

```python
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)
        positive_count = 0
        negative_count = 0

        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > 0:
                end = mid
            else:
                start = mid + 1
        positive_count = start # start가 음수에 가있음

        start = 0
        end = len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] >= 0:
                end = mid
            else:
                start = mid + 1
        negative_count = start - 1

        return  max(negative_count + 1, len(nums) - positive_count)
```
---

https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/

거리값 구하는 문제

절대값 구해서 d보다 크면 거리값 증가

arr1 요소가 arr2 요소보다 모두 d 이상으로 크면 카운트

69ms. Beats 80.30%

16.49MB. Beats 98.80%

O(logn)

```python
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = 0
        for num in arr1:
            left = 0
            right = len(arr2) - 1
            while left <= right:
                mid = (left + right) // 2
                if abs(num - arr2[mid]) <= d:
                    break
                elif num < arr2[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # break면 동작 안함
                res += 1
                
        return res
```
---
