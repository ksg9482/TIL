https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=python3

문자열 리스트에서 최소 최대 찾는 문제

음수 처리가 관건. 음수 부호도 문자열이라 고려해야 함

O(n). 
```python
def solution(s):
    answer = ''
    num_list = [int(num) for num in s.split(' ')]
    num_min = num_list[0]
    num_max = num_list[0]
    for i in range(1, len(num_list)):
        num_cur = num_list[i]
        if num_min > num_cur:
            num_min = num_cur
        elif num_max < num_cur:
            num_max = num_cur
    answer = f"{num_min} {num_max}"

    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/12951

문자열을 나누고 소문자로, 첫머리만 대문자로 바꾸는 문제

문자열 바꿀때 최대수 지정 조심할 것.

O(n)

```python
def solution(s):
    answer = ''
    for words in s.split(' '):
        if not words:
            answer += ' '
            continue
        temp = ''
        start = words[0]
        body = str(words).lower()
        if str(start).isalpha():
            body = body.replace(body[0], str(start).upper(), 1)
        temp += body
        answer += f' {temp}'
    return answer[1::]
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/12941

두 배열에서 값 뽑아 최소값 만드는 문제.

각각 오름차, 내림차로 정렬한 후 계산 한다

O(n)

```python
def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    for min_item, max_item in zip(A, B):
        answer += (min_item * max_item)

    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/12924

자연수 조합 찾는 문제. 투포인터.

합보다 작으면 오른쪽 이동, 크면 왼쪽 이동.

같으면 왼쪽 -> 합산 변하므로 지속적으로 파악

O(n)

```python
def solution(n):
    answer = 0
    left = 1
    right = 1
    sum_val = 1

    while left <= n // 2:
        if sum_val < n:
            right += 1
            sum_val += right
        elif sum_val > n:
            sum_val -= left
            left += 1
        else:
            answer += 1
            sum_val -= left
            left += 1

    return answer + 1
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/12911

숫자 비교하는 문제. n보다 큰 수를 찾는다. 단, 2진수로 바꾸면 1의 개수가 같아야 한다

반복문으로 대상 찾기. 

O(n)

```python
def solution(n):
    answer = 0
    n_count = format(n, 'b').count('1')
    target = n + 1
    while True:
        if n_count == format(target, 'b').count('1'):
            answer = target
            break
        target += 1

    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/12973

짝지어 제거할 수 있는 문자 나오면 제거하는 문제

스택으로 관리. 반복 후 스택에 없으면 다 제거된 것 

O(n)

```python
def solution(s):
    s_stack = deque()
    for i in s:
        if not s_stack:
            s_stack.append(i)
        elif s_stack[-1] == i: #바로 찾는거부터 나오면 에러
            s_stack.pop()
        else:
            s_stack.append(i)
    
    if not s_stack:
        return 1

    return 0
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/12914?language=python3

배열부터 미리 만들기. 어차피 2칸까지는 간단.

n칸 뛰고 1칸이나 2칸 뛰도록.

답은 1234567로 나눈 나머지여야 함 

O(n)

```python
def solution(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 2
    
    for i in range(2,n):
        dp[i] = dp[i-2] + dp[i-1]
	
    return dp[n-1] % 1234567
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/12953

최소공배수는 계속 관리해야 함. 누적됨

어차피 몫만 구하면 된다. 최소공배수 구하는 gcd이용

O(n)
```python
def solution(arr):
    answer = arr[0]

    for num in arr:
        answer = answer * num // gcd(answer, num)     

    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/138476

개수 세서 미리 사전만들기

정렬해서 연산

k가 0이 되면 종료

O(n)
```python
def solution(k, tangerine):
    answer = 0
    size_to_count = {}
    for i in tangerine:
        if i in size_to_count:
            size_to_count[i]+=1
        else:
            size_to_count[i]=1
    size_to_count = dict(sorted(size_to_count.items(), key=lambda x: x[1], reverse=True))
    for i in size_to_count:
        if k<=0:
            return answer
        k-=size_to_count[i]
        answer+=1

    return answer
```
---
https://school.programmers.co.kr/learn/courses/30/lessons/138476

괄호 짝짓는 문제. 스택으로 처리

어차피 괄호는 종류 고정. 그냥 함.

괄호 안열고 시작할 경우, 괄호 남은 경우 올바르지 않음

O(n)

```python
def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                stack.pop()
    if stack != []:
        return False
    return True
```
