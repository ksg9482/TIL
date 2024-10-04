https://school.programmers.co.kr/learn/courses/30/lessons/70129?language=python3

이진변환 반복하는 문제

0제거 -> 결과 문자열 길이를 다시 이진수로

위를 '1'만 남을때까지 반복

O(n)

```python
def solution(s):
    answer = [0,0] # 변환회수, 0개수
    while not s == '1':
        temp = ''
        for i in s:
            if i == '1':
                temp += i
            else:
                answer[1] += 1
        s = format(len(temp), 'b')
        answer[0] += 1
    return answer
```
---
"""
https://school.programmers.co.kr/learn/courses/30/lessons/12945?language=python3

피보나치 수 찾는 문제. 

n을 입력하면 n번째 피보나치 수를 1234567로 나눈 나머지를 반환.

O(n)
"""

```python
def solution(n):
    num_list = [0,1]
    for i in range(2, n + 1):
        num_list.append(num_list[i-2] + num_list[i-1])
    return num_list[-1] % 1234567
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/12980

순간이동이면 카운트 없음. 점프면 카운트 + 1

최대한 순간이동을 하면 카운트 최소. 짝수일 때만 가능하므로 짝수를 만든다

0될때까지 반복

O(n)

```python
def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
            ans += 1

    return ans
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/42885

그리디 문제. 정렬.

투포인터로 맨앞 맨뒤 같이 본 다음에 리미트 초과면 무거운 쪽부터. end만 조작

리미트 이하로 나오면 start, end 둘다.

O(n)

```python
def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people) - 1
    while start <= end:
        if people[start] + people[end] > limit:
            answer += 1
            end -= 1
        else:
            answer += 1
            start += 1
            end -=1
    
    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/12981

끝말잇기. 모듈러 연산으로 한바퀴 도는 것 체크. 

단어 체크는 사전으로 관리. 이미 있으면 중복이라 패배. 

순회수는 카운트로 관리

O(n)

```python
def solution(n, words):
    answer = [0,0]
    word_to_count = {words[0]:1}
    loop_count = 1
    prev = words[0]
    for i in range(1, len(words)):
        turn_idx = i % n
        if turn_idx == 0:
            loop_count += 1
        if word_to_count.get(words[i]) or not (prev[-1] == words[i][0]):
            answer = [turn_idx + 1, loop_count]
            break
        else:
            word_to_count[words[i]] = 1
        prev = words[i]
        
    return answer
```
---
https://school.programmers.co.kr/learn/courses/30/lessons/12985

두 변수 A, B가 n-1, n이 될때까지 n/2 반복하는 문제. 

A, B 두 변수가 소수면 올리기에 두 수가 같아지면 종료

O(n)

```python
def solution(n,a,b):
    answer = 0
    while True:
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1

        if a == b:
            break
        
    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3

프로세스 진행율을 큐로 관리하는 문제. 

[0]번째 요소가 완료되어야 이후 프로세스 진행. 100이상 되면 그 이후 100이상되는 모든 기능 한꺼번에 집계

한번에 몇개씩 집계되나 확인

O(n)

```python
def solution(progresses, speeds):
    answer = []
    while progresses:
        temp = 0
        if progresses[0] < 100:
            for i, (p, s) in enumerate(zip(progresses, speeds)):
                progresses[i] += s
        else:
            while progresses and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                temp += 1
            if temp:
                answer.append(temp)

    return answer
```
---
https://school.programmers.co.kr/learn/courses/30/lessons/131701

부분수열의 합 리스트를 구하는 문제.

원형 큐이므로 각 스타트 위치별로 부분수열이 생겨서 개수가 더 많아짐

중복 없는 합을 구하기에 set으로 답 관리

O(n)

```python
def solution(elements):
    answer = set()
    deq = deque(elements)
    for _ in range(len(deq)):
        val_sum = 0
        for e in deq:
            # deq[0] ... deq[0 + n]. 더한 부분수열 값 set으로.
            # 각 front에서 만들 수 있는 부분수열 합이 구해짐
            val_sum += e
            answer.add(val_sum)
        # 원형 큐 -> front 달라짐. front요소를 뒤로 보내 그 다음 순서 구현
        deq.append(deq.popleft())

    return len(answer)
'''
---

https://school.programmers.co.kr/learn/courses/30/lessons/76502

괄호 리스트를 한쪽으로 회전시킬 때 올바른 괄호 문자열이 몇개 나오는지 확인하는 문제

판단여부는 스택으로 확인

한번 끝났다고 마치는 게 아니라 결국 다 순회해서 확인해야 함.

순회 마치면 스택이 비어야 올바른 문자열.

O(n)

```python
def solution(s):
    answer = 0
    s_deq = deque(s)

    for _ in range(len(s_deq)):
        stack = deque()
        for i in s_deq:
            if i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            elif i == '(':
                stack.append(')')
            else:
                if not stack:
                    break
                if stack[-1] == i:
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1
        s_deq.append(s_deq.popleft())

    return answer
```
---
