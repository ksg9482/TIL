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

https://school.programmers.co.kr/learn/courses/30/lessons/131127?language=python3

10일간 원하는 아이템이 매칭되는지 확인하는 문제

제품, 수량이 일치하는 날 -> 10일 안에 다 포함되는 경우만 집계

원하는 아이템과 개수를 사전, 10일 간 아이템과 개수를 사전화

다 동일하면 +1. 없거나 다르면 다음.

O(n*m). want만큼 반복마다 순회해야 하고, 전체적으로 discount만큼 다 순회해야 함.

```python
def solution(want, number, discount):
    answer = 0
    item_to_want = {item: count for item, count in zip(want, number)}
    discount_to_item = {}
    discount_deq = deque()

    for item in discount:
        if len(discount_deq) >= 10:
            poped = discount_deq.popleft()
            discount_to_item[poped] -= 1
        if not discount_to_item.get(item):
            discount_to_item[item] = 1
        else:
            discount_to_item[item] += 1
        discount_deq.append(item)

        for wanted in item_to_want:
            if not item_to_want[wanted] == discount_to_item.get(wanted):
                break
        else:
            answer += 1
            
    return answer
```
---
https://school.programmers.co.kr/learn/courses/30/lessons/87390

n행, n열 2차원 배열

i행 i열까지 i로 채움

n행을 모두 이어붙여 1차원배열

arr[left] ... arr[right]만 남기고 제거

O(n^2). left, right에 맞춰서 끊었지만 본질적으로는 2차원 배열을 생성함. 찾아보니 1차원 배열로 바로 하는 솔루션이 정석인듯

```python
def solution(n, left, right):
    answer = []
    matrix = []
    left_start = left // n
    right_start = math.ceil(right / n)
    for i in range(left_start + 1, right_start + 2):
        temp = []
        for j in range(1,  n + 1):
            if i >= j:
                temp.append(i)
            else:
                temp.append(j)
        else:
            matrix.append(temp)
    answer = [y for x in matrix for y in x]
    start = left % n
    end = start + (right - left + 1)
    
    return answer[start:end]
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/12949

행렬곱 하는 문제이다. 조건은 간단하다. 행렬곱을 하는 것.

문제는 행렬곱을 그다지 접해본 적이 없다는 것이다. 

1. 두 행렬의 크기에 따라 생성된 행렬곱은 크기가 정해짐 -> 미리 만들어 놓을 수 있음

2. 사실상 곱을 누적하는 개념. 

행렬곱에 들어갈 위치에 값을 누산한다.

O(n*m)

```python
def solution(arr1, arr2):
    rows_arr1 = len(arr1)
    cols_arr1 = len(arr1[0])
    cols_arr2 = len(arr2[0])
    
    # 행렬곱이 수행된 리스트 크기는 정해져 있음.
    answer = [[0 for _ in range(cols_arr2)] for _ in range(rows_arr1)]
    
    for i in range(rows_arr1):
        for j in range(cols_arr2):
            for k in range(cols_arr1):
                # X축 * Y축으로 값을 구하고 지정된 그 값을 합산 -> 지정된 위치에 누산
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/17680

캐시를 구성하는 문제.

LRU로 캐시를 관리해야 하기 때문에 호출되지 않은 city를 구분해야 한다.

deque를 이용해서 호출된 city를 append. 호출되지 않은 city는 popleft 대상.

cache size가 0인 경우 엣지케이스 -> pop을 못함.

대소문자 구분 하지 않는 점도 중요.

O(n)

```python
def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    cities = [city.lower() for city in cities]
    for city in cities:
        if not city in cache:
            answer += 5
            if not cacheSize:
                continue
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)
        else:
            answer += 1
            poped = cache[cache.index(city)]
            cache.remove(city)
            cache.append(poped)

    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/64065

튜플을 구성하는 문제.

문자열을 리스트로 변환 -> 리스트를 튜플로 변환

배열의 순서가 달라도 같은 튜플이다. 단, 요소가 1개일 때는 그게 무조건 튜플 시작.

즉, 요소 1개일 때 리스트 삽입, 2개 일때 리스트에 없는 요소 삽입.... 반복

리스트를 계속 순회하는 것은 비효율적이니 사전으로 관리한다. 사전은 순서가 보장된다.

요소를 오름차순으로 정렬 -> 정렬대로 사전에 등록되기에 사전 순서가 곧 튜플 순서.

O(n)

```python
def solution(s):
    answer = []
    tuple_key_to_idx = {}
    str_lists = [i.split(',') for i in s[2:-2].split('},{')]
    str_lists.sort(key=lambda x: len(x))
    for str_list in str_lists:
        for idx, str_num in enumerate(str_list):
            if tuple_key_to_idx.get(str_num) == None:
                tuple_key_to_idx[str_num] = idx
    for tuple_val in tuple_key_to_idx.keys():
        answer.append(int(tuple_val))

    return answer
```
---
https://school.programmers.co.kr/learn/courses/30/lessons/17677

자카드 유사도 구하는 문제. 단, 부분집합으로 계산해야 바로 set에 넣지는 못한다.

전처리 후 카운터로 숫자 집계.

카운터 객체를 이용해서 교집합, 합집합 생성.

O(n)

```python
def solution(str1, str2):
    two_split_str1 = [str1[i-1:i+1] for i in range(1, len(str1))]
    two_split_str2 = [str2[i-1:i+1] for i in range(1, len(str2))]
    two_split_str1 = [s.lower() for s in filter(lambda s:s.isalpha(), two_split_str1)]
    two_split_str2 = [s.lower() for s in filter(lambda s:s.isalpha(), two_split_str2)]

    counter1 = Counter(two_split_str1)
    counter2 = Counter(two_split_str2)
    inter = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/43165

숫자 리스트의 일부를 음수로 바꾸며 누산 했을 때 타겟과 동일한 수가 나오는지 확인하는 문제

분류가 dfs / bfs.

처음은 양수만 있으니 음수로 하나씩 바꿔간다

O(n)

```python
def solution(numbers, target):
    def dfs(numbers, target, depth):
        answer = 0
        if depth == len(numbers): # leave
            # 끝까지 간걸로 다 더한다
            if sum(numbers) == target:
                return 1
            else:
                return 0
        else:
            # 먼저 양수 보내고 다음에 음수 보내면 양수, 음수로 점점 늘어감.
            answer += dfs(numbers, target, depth + 1)
            numbers[depth] *= -1 # 한칸씩 음수로 만들어 간다
            answer += dfs(numbers, target, depth + 1)
            return answer
        
    return dfs(numbers, target, 0)
```
---
https://school.programmers.co.kr/learn/courses/30/lessons/87946

완전탐색. 경우의 수를 다 따져봐서 해답을 구한다

dfs로 진행하되, 이미 방문한 요소를 체크.

dfs는 카운트를 따로 설정해서 최대한 depth를 내려가고 갱신되면 해답도 갱신

O(n)

```python
def solution(k, dungeons):
    global answer
    answer = 0
    visited = [0]*len(dungeons)

    def dfs(k, cnt, dungeons):
        global answer
        if cnt > answer:
            answer = cnt
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = 1
                dfs(k-dungeons[i][1], cnt + 1, dungeons)
                # dfs로 진행이 끝난 후 visited를 초기화 -> 백트래킹
                visited[i] = 0

    dfs(k, 0, dungeons)

    return answer
```
