https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

R, L의 균형 체크 문제

균형 맞는 순간만 체크하면 된다

균형체크용 카운터, 반환용 카운터 2개 둬서 사용

33ms. Beats 73.15%

16.44MB. Beats 54.62%

O(n).

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s) == 2:
            return 1
        b_count = 0
        count = 0
        for i in s:
            if i == "R":
                count += 1
            if i == "L":
                count -= 1
            if count == 0:
                b_count += 1
        return b_count
```
---

https://leetcode.com/problems/maximum-odd-binary-number/description/

2진수로 가장 큰 홀수 조합을 만들어야 함 

기본 8,4,2,1 이므로 1에 해당하는 부분에 1개를 소모. 그래야 홀수

나머지는 1개수만큼 앞에서부터 채운다

32ms. Beats 89.72%

16.49MB. Beats 74.58%

O(n).

```python
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        ans = ""
        for i in s:
            if i == "1":
                count += 1
        for j in range(len(s) - 1):
            if j < count - 1:
                ans += "1"
            else:
                ans += "0"
                
        # 맨마지막에 + 1해서 홀수화
        ans += "1"
        return ans
```
---

https://leetcode.com/problems/maximum-69-number/description/

숫자를 한 번만 바꿔서 가장 큰 수를 찾는 문제

타겟이 되는 수를 만나면 바로 교환한다.

문자열을 앞, 바뀌는 몸통, 뒤로 구분해서 합친다.

결과는 int로 바꿔서 반환

31ms. Beats 78.25%

16.52MB. Beats 13.89%

O(n).

```python
class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        for idx, s_num in enumerate(str_num):
            if s_num == "6":
                head = str_num[0:idx]
                body = "9"
                tail = str_num[idx + 1::]

                s_ans = head + body + tail

                return int(s_ans)
        return num
```
---

https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

가장 큰 합을 찾는 문제. 정렬해서 가장 큰 수를 기준으로 프로세스 진행

가장 큰 수에 +i 해서 계속 연산

141ms. Beats 72.24%

16.46MB. Beats 82.69%

O(nlogn). 정렬 수행.

```python
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums, reverse=True)

        ans = 0

        for i in range(k):
            ans += sorted_nums[0] + i

        return ans
```
---

https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/

리스트를 오름차순으로 커지게 만드는 문제. 단, 리스트 반환이 아니라 필요한 계산 횟수 반환.

어차피 n보다 n+1이 더 커야하니까 1씩 더 커지게 하려면 얼마 필요한지 count로 집계하자

93ms. Beats 94.19%

17.27MB. Beats 46.11%

O(n).

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        prev = None
        for num in nums:
            if prev is None:
                prev = num
                continue
            if num <= prev:
                diff = (prev - num) + 1
                count += diff
                num += diff
            prev = num
        return count
```
---

https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/description/

한 사이클을 기준으로 이동, 입력중 하나를 선택하는 문제

조건에 맞지 않으면 이동, 조건에 맞으면 입력.

시계, 반시계 방향으로 회전 -> 알파벳 배열 리스트를 현재 인덱스를 기준으로 반으로 나눈다. 

움직일때 더 가까운 방향으로 회전.

회전시간만 구하고 어차피 입력은 1초 고정이니 제시된 문자열 길이만큼 나중에 더하면 될 듯 하다.

31ms. Beats 86.11%

16.52MB. Beats 26.33%

O(n).

```python
class Solution:
    def minTimeToType(self, word: str) -> int:
        alpha_list = string.ascii_lowercase
        current_pointer = 0
        alpha_mid = len(alpha_list) // 2
        count = 0
        for w in word:
            if alpha_list[current_pointer] != w:
                next_pointer = alpha_list.find(w)
                if abs(next_pointer - current_pointer) < alpha_mid:
                    count += abs(next_pointer - current_pointer)
                else:
                    count += (len(alpha_list) - abs(next_pointer - current_pointer))
                current_pointer = next_pointer
        return count + len(word)
```
---

https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/description/

트럭에 한번에 놓을 수 있는 유닛 총량을 구하는 문제.

박스가 아니라 그 안에 있는 유닛수를 구해야 함

큰거 부터 하고, 초과되면 종료

135ms. Beats 66.05%

16.82MB. Beats 90.77%

O(n).

```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # 큰거부터 처리한다 -> 정렬. [1]번째가 커야한다
        sorted_boxTypes = sorted(boxTypes, key=lambda x: -x[1])
        count = 0
        # 동시에 채울 수 있는 최대 수. 
        for box, units in sorted_boxTypes:
            if box <= truckSize:
                truckSize -= box # 트럭에 물건을 채웠으니 그만큼 여유 줄임
                count += box * units
            else:
                # box가 더 크면 truckSize 만큼 옮길 수 있음
                # 남은 공간만큼 넣기 -> 박스가 아니라 유닛수만 구하면 됨
                count += truckSize * units
                return count
        return count
```
---
https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/

배열의 0이 아닌 가장 작은 요소로 배열의 다른 요소를 뺀다

반복해서 0으로 만든다

정렬 -> 반복문의 현재 요소로 다른 요소 빼기

현재 인덱스 이전 요소는 이미 연산 종료 -> 순회하는 요소가 점점 줄어든다

38ms. Beats 61.56%

16.43MB. Beats 65.53%

O(nlogn). 정렬.

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        nums_len = len(sorted_nums)
        count = 0
        for idx, num in enumerate(sorted_nums):
            trigger = False
            sum_num = num
            for i in range(idx, nums_len):
                if sorted_nums[i] == 0:
                    continue
                if sorted_nums[i] > 0:
                    trigger = True
                    sorted_nums[i] -= num
                    sum_num += num

            if trigger and sum_num:
                count += 1

        return count
```
---

https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/description/

가장 큰 부분배열 합 반환

단, 부분배열의 요소 개수가 최소여야 함.

만약 최대 부분 배열과 나머지의 합이 같으면 이때는 부분배열의 요소 개수가 최대여야 함

정렬 -> 전체 합 미리 계산 & 큰 요소부터 합산. 전체합에선 그만큼 차감

61ms. Beats 59.47%

16.48MB. Beats 88.70%

O(nlogn). 정렬.
```python
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        sorted_nums = sorted(nums, reverse=True)
        origin_num_sum = sum(sorted_nums)
        target_num_sum = sorted_nums[0]
        ans = [sorted_nums[0]]

        for num in sorted_nums[1::]:
            if (origin_num_sum - target_num_sum) < target_num_sum:
                return ans
            target_num_sum += num
            ans.append(num)

        return ans
```
---

https://leetcode.com/problems/split-with-minimum-sum/description/

숫자를 둘로 나눠서 계산하는 문제

문자열 수를 번갈아가며 분할

분할된 문자열을 숫자로 변환하여 계산

27ms. Beats 93.02%

16.61MB. Beats 7.69%

O(nlogn). 정렬이 요구됨

```python
class Solution:
    def splitNum(self, num: int) -> int:
        num_list = [s_num for s_num in str(num)]
        num_list.sort()
        num_1 = ''
        num_2 = ''

        for idx, s_num in enumerate(num_list):
            if idx % 2 == 0:
                num_1 += s_num
            else:
                num_2 += s_num

        return int(num_1) + int(num_2)
```
---

https://leetcode.com/problems/apple-redistribution-into-boxes/description/

최소 몇개 박스가 필요한가?

1,3,2 -> 4,3,1,5,2 일 경우 4,5 두개만 쓰면 됨. 즉 큰 용량부터 채워서 몇개 박스를 점유하는가 카운트

정렬 -> 사과 총합보다 용량 총합이 많아질때까지 용량 더하기.

몇번 더해야 하나 카운트

42ms. Beats 69.37%

16.44MB. Beats 63.67%

O(nlogn). 정렬이 요구됨


```python
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sorted_capacity = sorted(capacity, reverse=True)
        apple_sum = sum(apple)
        cap_sum = 0
        count = 1

        for cap_size in sorted_capacity:
            cap_sum += cap_size

            if apple_sum <= cap_sum:
                return count

            count += 1

        return count
```
---

https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/

색깔별 첫등장, 가장 나중 등장 체크

첫등장중 가장 작은거 나중 등장중 가장 큰거로 계산

어차피 요소 적으니 반복문 2개로 비교해도 큰 문제 없을것이라 판단

35ms. Beats 90.09%

16.45MB. Beats 65.72%

O(n^2). 2중 반복문 사용

```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        colors_map = defaultdict(int)
        for idx, col in enumerate(colors):
            if colors_map[col]:
                colors_map[col][1] = idx
            else:
                colors_map[col] = [idx, idx]

        max_diff = 0

        for idx_1, key_1 in enumerate(colors_map):
            colors_map[key_1]
            for idx_2, key_2 in enumerate(colors_map):
                if idx_1 == idx_2:
                    continue

                cur_diff = abs(colors_map[key_1][0] - colors_map[key_2][1])

                if max_diff < cur_diff:
                    max_diff = cur_diff
        return max_diff
```
---

https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/description/

시간 변환하는 문제. 02:30 -> 04:35로 바꿀때 몇번 연산이 들어가야 하느냐

분으로 단위를 통일해서 계산한다

60, 15, 5, 1로만 계산 가능 -> 큰거부터 계산 들어간다

if문으로 분기해서 체크하는 걸 반복하면 될듯

35ms. Beats 61.92%

16.41MB. Beats 82.01%

O(n). 

```python
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        num_current = 0
        num_correct = 0
        count = 0
        
        for idx, (cur, cor) in enumerate(zip(current.split(':'), correct.split(':'))):
            if idx == 0:
                num_current += (int(cur) * 60)
                num_correct += (int(cor) * 60)
            else:
                num_current += int(cur)
                num_correct += int(cor)

        while num_current < num_correct:
            count += 1
            time_diff = num_correct - num_current

            if time_diff >= 60:
                num_current += 60
            elif time_diff >= 15:
                num_current += 15
            elif time_diff >= 5:
                num_current += 5
            else:
                num_current += 1

        return count
```
---

https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/description/

짝 -> 짝, 홀 -> 홀은 코스트 없음.

결국 짝, 홀로 다 모아두고 어느 한 쪽으로 병합해야함

가장 작은 값을 찾아야 함 -> 더 작은 쪽이 움직여야 한다

작은쪽의 개수를 반환한다

32ms. Beats 86.23%

16.58MB. Beats 41.92%

O(n).

```python
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_count = 0
        even_count = 0

        for i in position:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        return min(odd_count, even_count)
```
---

https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/

각 문자를 숫자에 균등히 배분하는게 좋다 

어차피 중복글자 없으니 8자리까진 +1, 그 다음 8자리 +2 방식으로 해도 되지 않을까?

배열 8개 만들어 놓고 하나씩 삽입하면 될거 같다.

각 배열의 요소로 합산하면 될듯?

34ms. Beats 69.57%

16.45MB. Beats 62.73%

O(n).

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        pad_num = 8
        pads = [[] for _ in range(8)]
        pad_idx = 0
        for idx, chr in enumerate(word):
            if idx % pad_num == 0:
                pad_idx = 0
            
            pads[pad_idx].append(chr)
            pad_idx += 1

        count = 0
        for pad in pads:
            add_num = 0
            # 리스트에 넣으면 요소가 합산되서 총 몇번 눌러야 하는지 모름
            # 배열 요소가 2라면 1+2 해서 처음 8번은 +1, 다음 8번은 +2로 합쳐줘야 함
            for i in range(len(pad)):
                add_num += (i + 1)
            count += add_num
        return count
```
---

https://leetcode.com/problems/largest-odd-number-in-string/description/

홀수인 하위 문자열을 반환하는 문제

하위 문자열을 만드는 것과 1자리 수로 홀수를 판단하는 것이 중요

36ms. Beats 98.11%

17.81MB. Beats 21.73%

O(n)

```python
class Solution:
    def largestOddNumber(self, num: str) -> str:
        # 홀짝 구분은 1자리수만 보면 됨. 

        for i in range(len(num) - 1, -1 ,-1):
            if not int(num[i]) % 2 == 0:
                return num[:i + 1]
        
        return ""
```
---

https://leetcode.com/problems/k-items-with-the-maximum-sum/description/

생성된 리스트의 합을 구하는 문제

그냥 순서대로 생성하고 집계하면 될거 같은데?

31ms. Beats 91.00%

16.57MB. Beats 27.43%

O(n)

```python
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        num_list = []
        for i in range(numOnes):
            num_list.append(1)
        for i in range(numZeros):
            num_list.append(0)
        for i in range(numNegOnes):
            num_list.append(-1)
        return sum(num_list[0:k])
```
---

https://leetcode.com/problems/k-items-with-the-maximum-sum/description/

2개씩 집계 -> 세번째는 제거

정렬하면 큰거부터 합치니 작은거 제거 가능

36ms. Beats 96.30%

16.49MB. Beats 69.26%

O(nlogn)

```python
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        sorted_cost = sorted(cost, reverse=True)

        count = 0
        num_list = []
        for cost in sorted_cost:
            if len(num_list) < 2: 
                num_list.append(cost)
            else:
                num_sum = sum(num_list)
                count += num_sum
                num_list = []

        return count + sum(num_list)
```
---
https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/

숫자를 1번 바꿀때 각각 최고, 최소 값을 구해 계산.

큰거 -> 앞을 9로 바꾸면 된다

작은거 -> 앞을 0으로 바꾸면 된다. 어차피 숫자 앞에 0 포함이면 자리수 작아진다

최대한 앞 자리를 0으로 바꾸면 된다는 뜻.

33ms. Beats 72.48%

16.41MB. Beats 56.59%

O(n)

```python
class Solution:
    def minMaxDifference(self, num: int) -> int:
        str_num = str(num)
        max_change_num = num
        min_change_num = 0

        for idx, num_chr in enumerate(str_num):
            if int(num_chr) < 9:
                max_change_num = str_num.replace(str_num[idx], "9")
                break

        for idx, num_chr in enumerate(str_num):
            if int(num_chr) > 0:
                min_change_num = str_num.replace(str_num[idx], "0")
                break

        return int(max_change_num) - int(min_change_num)
```
---

https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/

가장 긴 부분배열 반환하는 문제.

요소별 순회하면서 그룹비교

다른거만 모으기

56ms. Beats 72.80%

16.52MB. Beats 39.08%

O(n)

```python
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        cur_group = None
        for word, group in zip(words, groups):
            if not group == cur_group:
                ans.append(word)
                cur_group = group
        return ans
```
