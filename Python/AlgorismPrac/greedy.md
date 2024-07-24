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
