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

https://leetcode.com/problems/range-sum-query-immutable/

리스트에서 특정 구간의 합을 구하는 문제.

미리 계산해서 넣어놓고 범위 구한다.

start, end해서 end - start하면 된다

71ms. Beats 59.19%

20.17MB. Beats 47.79%

O(n)

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)
        #초기값 0 지우기
        self.sums = self.sums[1::]

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] if left == 0 else self.sums[right] - self.sums[left - 1]

```
---

https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/

[0:p] [p+1::]로 left, right를 만들어서 계산하는 문제

left는 포함된 0으로, right는 포함된 1로 합산한다.

어차피 0번째 부터 봐야 한다. 먼저 1번째부터 순회한번 해서 1개수 파악

다음에 포인터를 좌에서 우로 옮기면서 0 오면 left 증가, 1이면 right 감소

26ms. Beats 98.41%

16.56MB. Beats 41.58%

O(n)

```python
class Solution:
    def maxScore(self, s: str) -> int:
        left, right = s[0:1], s[1::]
        left_sum = 1 if left[0] == '0' else 0
        right_sum = 0
        for right_chr in right:
            if right_chr == '1':
                right_sum += 1
        max_score = left_sum + right_sum

        for i in range(len(right) - 1):
            if right[i] == '1':
                right_sum -= 1
            else:
                left_sum += 1
            temp_sum = left_sum + right_sum
            if temp_sum > max_score:
                max_score = temp_sum

        return max_score
```
---
https://leetcode.com/problems/maximum-population-year/description/

연도 레인지 사이에 가장 많은 인원이 있는 연도를 구하는 문제

birth, death로 리스트 만들어서 사전으로 관리

가장 구간 많은 연도가 인원 많은것.

가장 빠른 날짜이니 우선 정렬하고 체크한다

43ms. Beats 64.68%

16.62MB. Beats 12.78%

O(n*m)

```python
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        year_to_count_dict = defaultdict(int)
        max_year = 0
        count = 0
        for log in logs:
            year_range = range(log[0], log[1])
            for year in year_range:
                count += 1
                year_to_count_dict[year] += 1

        for idx, year in enumerate(year_to_count_dict):
            if idx == 0:
                max_year = year
                continue
            if year_to_count_dict[max_year] < year_to_count_dict[year]:
                max_year = year

        return max_year
```
---
https://leetcode.com/problems/find-pivot-index/description/

좌우 합이 같아지는 지점을 찾는 문제

좌:0, 우:sum해서 요소만큼 우에서 좌로 값 보낸다

120ms. Beats 70.64%

17.70MB. Beats 83.91%

O(n)

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)

        for idx, num in enumerate(nums):
            right -= num
            if left == right:
                return idx
            left += num
            
        return -1
```
---
