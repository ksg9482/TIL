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
