https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

유효한 계산식 문자열의 괄호 깊이를 찾는 문제. 가장 깊은 게 무엇인가

스택으로 넣어두다가 짝되는 게 있으면 스택에서 제거.

스택에 더 들어가면(길이가 길어기면) ans에 + 1. 

빠지는 건 무시. 가장 깊던 순간 찾음 됨

30ms. Beats 86.68%

16.62MB. Beats 18.13%

O(n)

```python
class Solution:
    def maxDepth(self, s: str) -> int:
        s_stack = deque()
        ans = 0
        for char in s:
            if char == "(":
                s_stack.append("(")
                if len(s_stack) > ans:
                    ans += 1
            elif char == ")":
                s_stack.pop()
        return ans
```
---

https://leetcode.com/problems/remove-outermost-parentheses/description/

가장 바깥쪽 괄호 제거하는 문제. 괄호 한쌍의 숫자가 맞아야 한다

카운트로 관리하다가 0되는 시점이 한 세트

슬라이싱 해서 바깥 제거하고 정답에 통합

38ms. Beats 62.87%

16.66MB. Beats 47.41%

O(n)

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        stack_count = 0
        idx_start = 0
        for idx, s_char in enumerate(s):
            if s_char == "(":
                stack_count += 1
            else:
                stack_count -= 1
            if stack_count == 0:
                ans += s[idx_start + 1:idx]
                idx_start = idx + 1

        return ans
```
---

https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/

가격 리스트로 할인 들어간 리스트 반환

요소는 자기 인덱스 이후의 요소만 할인으로 가져갈 수 있음

자기보다 작은 첫번째 요소를 할인으로 가져감

할인은 이미 다른 요소에서 이용한 인덱스도 중복으로 가능. 

38ms. Beats 98.41%

16.61MB. Beats 40.81%

O(n^2)

```python
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for idx, price in enumerate(prices):
            for i in range(idx + 1, len(prices)):
                if price >= prices[i]:
                    diff = price - prices[i]
                    ans.append(diff)
                    break
            else:
                ans.append(price)
        
        return ans
```
---

https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/

샌드위치와 학생을 매칭하는 문제

샌드위치를 분배할 수 없으면 거기서 끝

샌드위치를 줄 수 있는데 받을 학생이 없으면 어차피 학생들 줄 바꿔도 못준다.

특정 타입 학생중 하나하도 먼저 0되면 종료

36ms. Beats 80.34%

16.57MB. Beats 40.02%

O(n)

```python
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_counts = [0, 0]
        for student in students:
            student_counts[student] += 1

        for sandwiche in sandwiches:
            if student_counts[sandwiche] == 0:
                return sum(student_counts)
            
            student_counts[sandwiche] -= 1
        
        return 0
```
---

https://leetcode.com/problems/baseball-game/

지정된 룰에 맞게 점수 계산하는 문제

스택에 숫자 넣어가면서 계산. 숫자가 아닌 문자열은 계산식으로.

음수 포함해서 숫자만 거르는건 복잡하기에 문자열 케이스를 상단에서 처리.

남은건 자연히 숫자로 변환할 수 있는 문자열만.

41ms. Beats 75.07%

16.84MB. Beats 9.36%

O(n)

```python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        num_stack = deque()

        for operation in operations:
            if operation == "C":
                num_stack.pop()
            elif operation == "+":
                num_stack.append(num_stack[-1] + num_stack[-2])
            elif operation == "D":
                num_stack.append(num_stack[-1] * 2)
            else:
                num_stack.append(int(operation))

        return sum(num_stack)
```
---
