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
