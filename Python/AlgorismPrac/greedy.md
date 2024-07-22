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
