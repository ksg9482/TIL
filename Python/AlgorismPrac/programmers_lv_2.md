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
