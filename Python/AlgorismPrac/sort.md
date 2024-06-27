https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points

가장 넓은 넓이를 구하는 문제

연속된 요소의 값이 넓이 -> 연속된 요소의 차가 클수록 넓이도 넓음

[0]번째(x) 요소로 정렬한다. [1]번째(y) 요소는 넓이에 영향을 주지 않는다

가장 첫번째 요소의 경우 0에서 계산이 들어가기에 트리거를 채택해서 별도 계산은 하지 않도록했다. enumrate는 리스트를 반환하기에 그만큼 시간이 더 걸린다.

단순히 트리거 동작하는 방식이 더 빠를것이라 본다. 실제로 이 방법이 조금더 빨랐다.

686ms. Beats51.30%

59.16MB. Beats 53.17%

```python
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sorted_point = sorted(points, key=lambda x:x[0])

        max_vertical_area = 0
        prev = 0
        is_first = True

        for point in sorted_point:
            if is_first:
                prev = point[0]
                is_first = False
                continue

            current_vertical_area = abs(prev - point[0])

            if current_vertical_area > max_vertical_area:
                max_vertical_area = current_vertical_area

            prev = point[0]
        
        return max_vertical_area
```

---

https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

기본적으로 2자리 숫자끼리 더하는게 작다.

큰 수는 뒤에 있는게 작다. -> 가장 작은 수와 가장 큰 수를 더하는게 가장 작은 합이다

1. 수를 정렬([1,2,3,4])
2. 맨 앞과 맨 뒤 합치기, 남은 두개 합치기
    * 단, 큰 수가 뒤로 가야함(14, 23)
3. 이 둘 합친게 가장 작은 합

31ms. Beats 78.89%

16.40MB. Beats 65.05%

어차피 맨 앞과 맨 뒤를 타겟으로 하면서 가운데로 좁히는 방식이라면 투포인터를 적용할 여지가 있다고 보았다

O(nlogn).

```python
class Solution:
    def minimumSum(self, num: int) -> int:
        sorted_num_list = sorted(str(num))
        merge_list = []

        start = 0
        end = len(sorted_num_list) - 1
        while start < end:
            if sorted_num_list[start] < sorted_num_list[end]:
                merge_list.append(sorted_num_list[start] + sorted_num_list[end])
            else:
                merge_list.append(sorted_num_list[end] + sorted_num_list[start])
            start += 1
            end -= 1

        return int(merge_list[0]) + int(merge_list[1])
```

---

https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone

앉을 자리 구하기 -> 자기 자리에서 가장 가까운 자리에 앉게하는게 목적. 한번씩 이동하면 전체 몇번 움직이는가

자리, 학생 각각 정렬 -> 가까운 순으로 정렬되면 자기가 가까운 자리까지 가는데 얼마가 걸리는지 계산

54ms. Beats 86.20%

16.46MB. Beats 63.04%

O(nlogn).

```python
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        sorted_seats = sorted(seats)
        sorted_students = sorted(students)

        count = 0
        for i, student in enumerate(sorted_students):
            calc = abs(student - sorted_seats[i])
            count += calc

        return count
```
---

https://leetcode.com/problems/minimum-number-game

A와 B가 각각 리스트에서 최소를 뽑는다 (A, B순)

B와 A가 각각 결과 리스트에 삽입한다 (B, A순) 

1. 정렬 -> 최소 요소순으로 가져간다
2. 결과에 넣는건 가져온 순서의 역순

33ms. Beats 99.94%

16.50MB. Beats 78.95%

O(nlogn).

```python
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        ans = []
        for i in range(0, len(sorted_nums) - 1, 2):
            a_num = sorted_nums[i]
            b_num = sorted_nums[i + 1]

            ans.append(b_num)
            ans.append(a_num)
        return ans
```
---
https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description/

정렬 -> 최소+최대 / 2를 구해서 가장 작은 결과를 반환

정렬해서 투포인터로 접근한다

가장 첫번째 minimum에 들어갈 건 0번째와 마지막.

그 다음부터는 포인터를 1씩 더 옮겨서 시작한다

39ms. Beats 92.19%

16.55MB. Beats 41.85%

O(nlogn).

```python
class Solution:
    def minimumAverage(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        minimum = (sorted_nums[0] + sorted_nums[len(sorted_nums) - 1]) / 2
        start = 1
        end = len(sorted_nums) - 2

        while start < end:
            average = (sorted_nums[start] + sorted_nums[end]) / 2
            if minimum > average:
                minimum = average
            start += 1
            end -= 1

        return minimum
```
---
https://leetcode.com/problems/sorting-the-sentence/description/

문자와 숫자를 분리.

숫자를 기준으로 정렬.

문자는 다 합쳐 하나의 문자열로.

31ms. Beats 79.04%

16.41MB. Beats 53.56%

O(n*m). 정렬 안 했음. 하지만 for문 안에 슬라이싱이 있으므로 최악의 경우 O(n^2).

```python
class Solution:
    def sortSentence(self, s: str) -> str:
        ans = ""
        s_dict = {}
        splited_s = s.split(sep=" ")

        for s_text in splited_s:
            s_dict[s_text[-1]] = s_text[0:len(s_text) - 1]

        for i, s_text in enumerate(start=1, iterable=splited_s):
            # 띄어쓰기 구분용. 처음은 띄어쓰기가 없어야 함
            ans += f"{s_dict.get(str(i))}" if not ans else f" {s_dict.get(str(i))}" 

        return ans
```
---
