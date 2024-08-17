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
https://leetcode.com/problems/missing-number/description/

누락된 숫자 구하는 문제

0부터 n까지 리스트가 있다

그중 숫자 1개가 누락되고, 그 누락된 수를 찾는다

맞닺은 요소 2개를 뺐을 때 0보다 작으면 누락

114ms. Beats 45.91%

17.73MB. Beats 49.50%

O(nlogn)

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            # 오름차순 1씩 증가 -> 어긋나면 그게 없는거
            if nums[mid] - (mid + 1) < 0:
                start = mid + 1
            else:
                end = mid - 1
        
        return start
```
---

https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

두 요소 합산해서 타겟보다 작은 값으로 카운트 구하기

타겟이 맞으면 left 상승. 아니면 right 다운

48 ms. Beats 61.95%

16.54 MB. Beats 31.11%

O(nlogn)

```python
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count
```
---

https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/

1이 끝나는 부분까지 포인터 가져온다

포인터가 1의 개수. 인덱스와 함께 리스트에 넣고 정렬.

k만큼 뽑아낸다

92ms. Beats 75.40%

16.90MB. Beats 68.25%

O(nlogn)

```python
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat_list = []
        for idx, inners in enumerate(mat):
            start = 0
            end = len(inners) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if inners[mid] == 1:
                    start = mid + 1
                else:
                    end = mid - 1
            mat_list.append((start, idx))
        mat_list.sort()
        return [mat_list[i][1] for i in range(k)]
```
---

https://leetcode.com/problems/intersection-of-two-arrays/description/

배열 2개 교집합 구하기. 단, 중복 없이

배열 1개 기준으로 타겟 삼아서 이진 검색. 내용 있으면 set에 삽입

set 반환

44ms. Beats 78.86%

16.74MB. Beats 23.94%

O(nlogn)
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        nums2.sort()

        for num_1 in nums1:
            start = 0
            end = len(nums2) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums2[mid] == num_1:
                    ans.add(nums2[mid])
                    break
                elif nums2[mid] <= num_1:
                    start = mid + 1
                else:
                    end = mid - 1
                
        return list(ans)
```
---
https://leetcode.com/problems/count-complete-tree-nodes/description/

노드가 전부 몇 개인지 세는 문제. 단 O(n)보다 빨라야 한다

좌우 각각 계산한다.

좌우가 같으면 서로 같은 뎁스라는 뜻.

다르면 재귀로 계산

39ms. Beats 99.48%

21.56MB. Beats 95.78%

O(logn)

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l_count = 0
        left = root.left
        while left:
            l_count += 1
            left = left.left

        r_count = 0
        right = root.right
        while right:
            r_count += 1
            right = right.right

        if l_count == r_count:
            return 2**(l_count + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```
---

https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/

x찾는 문제

x가 2이면 리스트에 2보다 크거나 같은 수가 2개 있어야 한다

이진검색으로 타겟보다 작은수 인덱스 찾기. len - 인덱스 하면 몇개인지 나옴

크거나 같으면 start로 옮김. 가장 앞으로 가야한다.

35ms. Beats 83.76%

16.45MB. Beats 68.40%

O(nlogn)

```python
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        num_len = len(nums)
        for target_num in range(num_len + 1):
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] >= target_num:
                    end = mid - 1
                else:
                    start = mid + 1
            if len(nums) - start == target_num:
                return target_num
            
        return -1
```
---
https://leetcode.com/problems/fair-candy-swap/description/

총 수를 구해서 각각 몇개씩 가져야 하는지 계산

순서대로 하나씩 주었을때 목적하는 수와 같은 수가 있다면 그걸 주면 된다

[1,1] [2,2]가 있으면 먼저 1 타겟. 총수는 6. 구해야 하는 수는 3.

1을 주면 받은 쪽은 5가됨. 5 - 3 하면 2.

2를 가지고 있으면 그걸 주면 됨

답 [1, 2]

이진검색을 하면 더 빨라질 수가 없을듯. 

솔루션 봐도 이진검색보다는 다른 방법 이용.

343ms. Beats 31.36%

18.36MB. Beats 98.63%

O(nlogn)

```python
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        bobSizes.sort()
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2

        for alice_num in aliceSizes:
            start = 0
            end = len(bobSizes) - 1
            target_num = alice_num - diff
            while start <= end:
                mid = (start + end) // 2
                if (bobSizes[mid]) == target_num:
                    return [alice_num, bobSizes[mid]]
                elif (bobSizes[mid]) < target_num:
                    start = mid + 1
                else:
                    end = mid - 1
```
