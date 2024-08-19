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
---

https://leetcode.com/problems/kth-missing-positive-number/

누락된 k번째 수를 찾는 문제.

k번째가 진행되는 만큼 start도 꾸준히 올라감

그 이상으로 가기 전까지 start 올리고 그 기준으로 k 합산

52ms. Beats 54.20%

16.71MB. Beats 17.41%

O(logn)

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = end - (end - start) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                start += mid + 1
            else:
                end = mid - 1
        return start + k
```
---

https://leetcode.com/problems/minimum-common-value/description/

공통 최소 정수 찾는 문제

공통 있으면 해당 정수 반환

공통 없으면 -1 반환.

하나씩 이진 검색으로 찾기.

341ms. Beats 71.69%

34.86MB. Beats 68.47%

O(nlogm). 하나씩 순회 + 이진검색으로 찾기

```python
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        # 두 리스트를 일괄처리하기 위해 input 조정. 더 적은게 앞에 가야 함
        if nums1_len > nums2_len:
            return self.getCommon(nums2, nums1)
        prev=0
        for i in nums1:
            j = bisect_left(nums2, i, lo=prev)
            if j==nums2_len: 
                return -1
            elif i==nums2[j]: 
                return i
            else: 
                prev=j
        return -1
```
---

https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

두 배열의 교집합 리스트를 반환하는 문제

이진 검색으로 찾기. 결국 핵심은 요소를 다른 배열에 검색하는 방식.

49ms. Beats 52.91%

16.75MB. Beats 26.01%

O(nlogm). 하나씩 순회 + 이진검색으로 찾기

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        nums1.sort()
        nums2.sort()
        ans = []
        l = 0
        r = len(nums2) - 1

        for num in nums1:
            i = self.binarySearch(nums2, l, r, num)
            if i != -1:
                l = i + 1
                ans.append(num)
        
        return ans
    
    def binarySearch(self, a, l, r, x):
        while l <= r:
            m = (l + r) // 2
            while m - 1 >= l and a[m - 1] == x:
                m -= 1
            if a[m] == x:
                return m
            if a[m] > x:
                r = m - 1
            else:
                l = m + 1
        return -1
```
---

https://leetcode.com/problems/binary-search/description/

전통적인 이진검색 문제.

값이 있으면 인덱스를 반환하고 없으면 -1을 반환한다.

185ms. Beats 84.63%

18.09MB. Beats 67.00%

O(logn)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid + 1

        if nums[start] != target:
            return -1
        return start
```
---

https://leetcode.com/problems/binary-search/description/

미리 선언된 함수를 이용해서 값을 추론하는 문제

guess함수 반환값에 따라 up, down을 정해서 이진검색 실시

36ms. Beats 46.42%

16.41MB. Beats 56.07%

O(logn)

```python
class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n
        while start <= end:
            mid = start + (end - start) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1: # -1이면 더 높음. 내려가야 함
                end = mid - 1
            else: # 1이면 더 낮음. 올라가야 함
                start = mid + 1
        return -1
```
---

https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

타겟보다 작은 글자 찾는 문제.

알파벳을 기준으로 한다. 있으면 그대로 반환하고 없으면 첫번째 문자 반환한다.

문자열끼리 비교 가능. 문자열 비교 이용한다. 

105ms. Beats 62.44%

16.79MB. Beats 91.23%

O(logn).

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters)
        
        while start < end:
            mid = (start + end) // 2
            if letters[mid] > target:
                end = mid
            else:
                start = mid + 1
        return letters[end] if end < len(letters) else letters[0]
```
---

https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/

부분 시퀸스를 미리 만들어 놓고 이진 검색

98ms. Beats 55.58%

16.88MB. Beats 68.59%

```python
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = [0]*len(queries)
        # 부분 시퀸스 생성
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        # 각 부분 시퀸스로 판단
        for i, query in enumerate(queries):
            idx = -1
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start+end)//2
                if nums[mid]<=query:
                    idx = mid
                    start = mid+1
                else:
                    end = mid-1

            ans[i] = idx + 1

        # 가장 긴 부분시퀸스 반환
        return ans
```
---

https://leetcode.com/problems/search-insert-position/description/

리스트에 삽입할 장소를 찾는 문제.

이진 검색으로 값이 있으면 그 인덱스 반환.

없으면 순서대로 증가하도록 삽입하고 그 인덱스 반환.

50ms. Beats 52.87%

17.40MB. Beats 15.61%

O(logn).

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start = 0
        end = length - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        # 삽입할 장소가 앞에 있다는 의미.
        if start > end: 
            return end + 1
        
        return length
```
---

https://leetcode.com/problems/first-bad-version/description/

api 호출해서 그 값으로 이진검색 하는 문제

사실상 True가 나오는 가장 작은 수를 찾는다.

True 안나올 때까지 end 감소. False 나오면 start 증가.

균형 맞는 부분이 답

34ms. Beats 59.36%

16.38MB. Beats 87.40%

O(logn).

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n
        mid = n // 2

        while start < end:
            # 앞은 False여야 함
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
            mid = (start + end) // 2
                
        return start
```
