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
