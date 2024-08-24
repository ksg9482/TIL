https://leetcode.com/problems/left-and-right-sum-differences/description/

좌우 요소 합산으로 절대값 계산하는 문제

좌우 방향만 다르지 요소 수는 같으므로 투포인터로 동시 처리.

59ms. Beats 84.33%

16.90MB. Beats 43.86%

O(n)

```python
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sums, right_sums = deque([0]), deque([0])
        ans = []
        left, right = 0, len(nums) - 1
        limit = len(nums) - 1
        current_left = 0
        current_right = 0
        while left < limit:
            current_left += nums[left]
            current_right += nums[right]
            left_sums.append(current_left)
            right_sums.appendleft(current_right)
            left += 1
            right -= 1
        while left_sums:
            ans.append(abs(left_sums.popleft() - right_sums.popleft()))

        return ans
```
---

https://leetcode.com/problems/running-sum-of-1d-array/description/

리스트 순회하면서 요소 합산하는 문제.

정답 배열에 n[0]을 미리 넣어두고 순회를 1번째 인덱스부터 시작.

정답배열[-1]에 현재 값을 더해 넣는다

33ms. Beats 94.70%

16.75MB. Beats 28.75%

O(n)

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(ans[-1] + nums[i])
        return ans
```
---

https://leetcode.com/problems/find-the-pivot-integer/description/

1부터 n까지 양의 정수로 이루어진 리스트를 나눠서 그 합이 같도록 하는 문제.

좌, 우에 똑같이 들어가면서 양 합이 같도록 한다 -> 이진 검색으로 찾으면 될거 같다

pivot integer를 x라고 했을 때 [0:x + 1], [x::]했을 때 값이 같으면 된다

46ms. Beats 61.38%

16.47MB. Beats 72.84%

O(logn)

```python
class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = [num + 1 for num in range(n)]
        start = 0
        end = n - 1
        
        while start <= end:
            mid = (end + start) // 2
            left_sum = sum(nums[0:mid + 1])
            right_sum = sum(nums[mid::])
            if left_sum == right_sum:
                return nums[mid]
            elif left_sum > right_sum:
                end = mid - 1
            else:
                start = mid + 1

        return -1
```
---

https://leetcode.com/problems/find-the-highest-altitude/description/

nums[n] + nums[(n+1)] 중 가장 큰 값을 고르는 문제

누적값을 current로 관리하면서 새로운 값과 비교.

더 큰값을 ans에 할당한다. 이것을 순회 마칠때까지 반복

34ms. Beats 81.90%

16.42MB. Beats 61.70%

O(n)

```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        highest = 0
        for num in gain:
            current += num
            if current > highest:
                highest = current
        return highest
```
---


https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/

홀수개 부분배열을 더한 합을 구하는 문제

홀수개씩 슬라이스 해서 더하기 -> 이러니까 O(n^3)나옴. 56ms. Beats 51.02%

빈도수로 찾는 솔루션으로 전환.

부분배열에 해당 요소가 몇번 들어가냐를 찾으면 됨

35ms. Beats 93.85%

16.54MB. Beats 40.93%

O(n)

```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr_len = len(arr)
        result = 0
        
        for i in range(arr_len):
            start = arr_len - i
            end = i + 1
            total = start * end
            odd = (total + 1) // 2
            result += odd * arr[i]
        
        return result
```
---
https://leetcode.com/problems/ant-on-the-boundary/description/

포인터가 좌우로 이동하다가 0지점에서 멈춘 횟수를 세는 문제

넘어간건 세지 않는다

42ms. Beats 66.67%

16.57MB. Beats 20.33%

O(n)

```python
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = 0
        pointer = 0
        for num in nums:
            pointer += num
            if pointer == 0:
                ans += 1

        return ans
```
---

https://leetcode.com/problems/find-the-middle-index-in-array/description/

특정 인덱스를 기준으로 좌우가 같은 지점을 찾는 문제

좌 인덱스에서 이동.

가장 왼쪽 요소를 반환해야 하니 왼쪽부터 해야 편함

37ms. Beats 86.01%

16.44MB. Beats 74.84%

O(n)

```python
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        mid = 0
        while mid < len(nums):
            left_sum = sum(nums[0:mid])
            right_sum = sum(nums[mid + 1::])
            if left_sum == right_sum:
                return mid
            else:
                mid += 1

        return -1
```
---

https://leetcode.com/problems/find-the-middle-index-in-array/description/

요소 계산할 때 +1 되도록 startValue에 더하기.

음수면 양수가 되도록 가공해서 넣는다

음수로 떨어지는 결과값에서 +1 만큼만 커져도 됨

30ms. Beats 91.22%

16.45MB. Beats 62.44%

O(n)

```python
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        num_sum = 0
        min_start_value = 1
        
        for num in nums:
            num_sum += num
            # 차이값. 1미만이 나오면 안됨 -> 기존값이 더 크면 유지
            # 음수면 그보다 1보다 커야함 -> 1 - (-n)이 되서 1더한 값이랑 비교
            min_start_value = max(min_start_value, 1-num_sum)

        return min_start_value
```
---
