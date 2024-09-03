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

https://leetcode.com/problems/next-greater-element-i/description/

num1[i]와 같은 요소를 num2에서 찾고 그 인덱스 기준으로 더 큰 수를 찾는 문제

유니크한 값이니 사전으로 관리할 수 있을듯

40ms. Beats 93.25%

16.79MB. Beats 69.27%

O(n^2). 최악 모든 요소가 맨 끝까지 가야함

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_next_dict = defaultdict(int)
        ans = []
        for i in range(1, len(nums2)):
            next_idx = i
            while next_idx < len(nums2):
                if nums2[i - 1] < nums2[next_idx]:
                    num_to_next_dict[nums2[i - 1]] = nums2[next_idx]
                    break
                next_idx += 1
        
        for num_1 in nums1:
            next_num = num_to_next_dict.get(num_1)
            if next_num is None:
                ans.append(-1)
            else:
                ans.append(next_num)

        return ans
```
---

https://leetcode.com/problems/clear-digits/description/

문자는 스택에 넣고 숫자 오면 pop해서 최종 결과 만드는 문제

deque에 넣어서 관리하다가 "".join()으로 문자열화 해서 반환한다

36ms. Beats 66.35%

16.52MB. Beats 23.74%

O(n)

```python
class Solution:
    def clearDigits(self, s: str) -> str:
        chars = deque()
        for s_char in s:
            if s_char.isalpha():
                chars.append(s_char)
            else:
                chars.pop()
        
        return "".join(chars)
```
---
https://leetcode.com/problems/crawler-log-folder/

경로를 스택에 넣어 관리하다 마지막 길이를 구하는 문제.

현재 경로에서 처음경로까지는 결국 스택에 몇개 들었나를 보는 것.

47ms. Beats 73.02%

16.64MB. Beats 75.28%

O(n)

```python
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        path_stack = deque()
        for log in logs:
            if log == "../":
                if len(path_stack) >= 1:
                    path_stack.pop()
            elif log == "./":
                pass
            else:
                path_stack.append(log)
                    
        return len(path_stack)
```
---

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

스택 이용.

중복 확인하면서 맨 마지막과 비교

51ms. Beats 92.31%

17.26MB. Beats 80.47%

O(n)

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
```
---

https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/

스택 이용.

입력 문자와 이전문자로 타겟되는 문자열 만들어지면 제거.

40ms. Beats 80.11%

16.43MB. Beats 77.74%

O(n)

```python
class Solution:
    def minLength(self, s: str) -> int:
        s_stack = deque(s)
        ans = deque()

        while s_stack:
            s_char = s_stack.popleft()
            if ans and (ans[-1] == "A" and s_char == "B"):
                ans.pop()
            elif ans and (ans[-1] == "C" and s_char == "D"):
                ans.pop()
            else:
                ans.append(s_char)

        return len(ans)
```
---

https://leetcode.com/problems/make-the-string-great/description/

스택 이용.

연속된 입력문자 2개가 동일한 문자의 대-소문자 또는 소-대문자인 경우 제거한다

사전에 {알파벳 : 인덱스}로 넣는다

두 문자의 차 절대값이 26이면 동일 문자

30ms. Beats 94.10%

16.61MB. Beats 28.86%

O(n)

```python
class Solution:
    def makeGood(self, s: str) -> str:
        ans = deque()
        stack = deque(s)
        letter_to_idx_dict = defaultdict(int)
        for idx, letter in enumerate(string.ascii_letters):
            letter_to_idx_dict[letter] = idx
        
        while stack:
            s_char = stack.popleft()
            if ans and (abs(letter_to_idx_dict.get(ans[-1]) - letter_to_idx_dict.get(s_char)) == 26):
                ans.pop()
            else:
                ans.append(s_char)
        
        return "".join(ans)
```
---

https://leetcode.com/problems/implement-stack-using-queues/description/?envType=problem-list-v2&envId=stack&difficulty=EASY

큐 2개로 스택 구현체 만드는 문제

파이썬 동작이 아니라 일반적인 스택 동작에 맞추어 구현

31ms. Beats 79.48%

16.62MB. Beats 32.57%

O(n). 큐 2개로 데이터를 옮겨야 해서 n이 클수록 늘어남

```python
class MyStack:

    def __init__(self):
        self.queue_1 = deque()
        self.queue_2 = deque()

    def push(self, x: int) -> None:
        self.queue_1.append(x)

    def pop(self) -> int:
        while len(self.queue_1) > 1:
            self.queue_2.append(self.queue_1.popleft())
        
        poped = self.queue_1.popleft()

        while self.queue_2:
            self.queue_1.append(self.queue_2.popleft())
        
        return poped

    def top(self) -> int:
        while len(self.queue_1) > 1:
            self.queue_2.append(self.queue_1.popleft())
        
        top_value = self.queue_1[0]

        self.queue_2.append(self.queue_1.popleft())

        while self.queue_2:
            self.queue_1.append(self.queue_2.popleft())
        
        return top_value

    def empty(self) -> bool:
        return len(self.queue_1) == 0
```
---

https://leetcode.com/problems/implement-queue-using-stacks/?envType=problem-list-v2&envId=stack&difficulty=EASY

스택 2개로 큐 구현체 만드는 문제

파이썬 동작이 아니라 일반적인 큐 동작에 맞추어 구현

34ms. Beats 63.00%

16.73MB. Beats 30.33%

O(n). 스택 2개로 데이터를 옮겨야 해서 n이 클수록 늘어남

```python
class MyQueue:

    def __init__(self):
        self.stack_1 = deque()
        self.stack_2 = deque()

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        while len(self.stack_1) > 1:
            self.stack_2.append(self.stack_1.pop())
        
        poped = self.stack_1.pop()

        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        
        return poped

    def peek(self) -> int:
        while len(self.stack_1) > 1:
            self.stack_2.append(self.stack_1.pop())
        
        peeked = self.stack_1[0]

        self.stack_2.append(self.stack_1.pop())

        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        
        return peeked

    def empty(self) -> bool:
        return len(self.stack_1) == 0
```
---

https://leetcode.com/problems/palindrome-linked-list/description/?envType=problem-list-v2&envId=stack&difficulty=EASY

스택으로 팰린드롬 여부 확인하는 문제

스택에 먼저 넣어두고 원본, 스택 대조하며 확인.

다른거 나오면 팰린드롬 아님.

289ms. Beats 64.29%

37.01MB. Beats 25.36%

O(n)

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = deque()
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        
        node = head
        while stack:
            stack_val = stack.pop()
            if not stack_val == node.val:
                return False
            node = node.next
        
        return True
```
---
https://leetcode.com/problems/backspace-string-compare/?envType=problem-list-v2&envId=stack&difficulty=EASY

스택으로 관리

문자열 에서 # 나오면 이전 문자 pop 한다

문자열 길이 관리가 더 신경쓸게 많음

32ms. Beats 77.02%

16.47MB. Beats 74.45%

O(n)

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = deque()
        stack_2 = deque()
        
        for s_char in s:
            if stack and s_char == "#":
                stack.pop()
            elif not s_char == "#":
                stack.append(s_char)

        for t_char in t:
            if stack_2 and t_char == "#":
                stack_2.pop()
            elif not t_char == "#":
                stack_2.append(t_char)
        
        while stack and stack_2:
            if not (stack.pop() == stack_2.pop()):
                return False

        return len(stack) == 0 and len(stack_2) == 0
```
