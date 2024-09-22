https://school.programmers.co.kr/learn/courses/30/lessons/178871

달리기. 이름 부르면 바로 앞 선수와 순위가 바뀐다

리스트에서 요소 서로 교환하는 방식으로 처리

순서 인덱스 바로 찾도록 사전으로 순서 관리

```python
def solution(players, callings):
    player_to_num_dict = defaultdict(int)
    for idx, player in enumerate(players):
        player_to_num_dict[player] = idx
    for calling in callings:
        called_idx = player_to_num_dict[calling]
        target_idx = called_idx - 1
        players[called_idx], players[target_idx] = players[target_idx], players[called_idx]
        player_to_num_dict[players[called_idx]] += 1
        player_to_num_dict[players[target_idx]] -= 1

    return players
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/176963

리스트별로 집계하는 문제. 타겟과 점수를 사전으로 묶는다

사전에 넣은 점수로 가져와서 합산. 없는 인원 부르니 get으로 가져오기

O(n*m). photo가 길면 길어짐. photo는 이중배열이므로 외부 내부 다 영향 받음

```python
def solution(name, yearning, photo):
    answer = []
    name_to_value_dict = defaultdict(int)
    for n, y in zip(name, yearning):
        name_to_value_dict[n] = y
    for p in photo:
        sum_value = 0
        for p_name in p:
            value = name_to_value_dict.get(p_name)
            if value:
                sum_value += value
        answer.append(sum_value)

    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/172928

위치 시뮬레이션 하는 문제

2차원 배열에서 시작점 찾기 -> 명령 이행 -> 결과 반환

명령은 수행할 수 없는 경우 무시된다.

O(n). 명령이 길수록 시간 걸림

```python
def solution(park, routes):
    park_map = []
    dog = [] # [세로, 가로]
    for i, p_str in enumerate(park):
        temp = []
        for j, p in enumerate(p_str):
            if p == "S":
                dog.append(i)
                dog.append(j)
            temp.append(p)
        park_map.append(temp)
    for route in routes:
        command = route.split(" ")
        command[1] = int(command[1])
        if command[0] == "N":
            for i in range(1, command[1] + 1):
                if dog[0] - i < 0:
                    break
                if park_map[dog[0] - i][dog[1]] == "X":
                    break
            else:
                dog[0] -= command[1]
        elif command[0] == "S":
            for i in range(1, command[1] + 1):
                if dog[0] + i >= len(park_map):
                    break
                if park_map[dog[0] + i][dog[1]] == "X":
                    break
            else:
                dog[0] += command[1]
        elif command[0] == "W":
            for i in range(1, command[1] + 1):
                if dog[1] - i < 0:
                    break
                if park_map[dog[0]][dog[1] - i] == "X":
                    break
            else:
                dog[1] -= command[1]
        elif command[0] == "E":
            for i in range(1, command[1] + 1):
                if dog[1] + i >= len(park_map[0]):
                    break
                if park_map[dog[0]][dog[1] + i] == "X":
                    break
            else:
                dog[1] += command[1]

    return dog
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/161990

2차원 배열에서 최소, 최대 지점 찾는 문제

최소는 0, 0을 기준으로 하지만 최대는 타겟을 건너가야 하기 때문에 x,y에 +1씩 해준다

O(n)

```python
def solution(wallpaper):
    answer = [-1, -1, -1, -1] # min_y, min_x, max_y + 1, max_x + 1
    for y_idx, rows in enumerate(wallpaper):
        for x_inx, col in enumerate(rows):
            if col == "#":
                if answer[0] == -1:
                    answer[0] = y_idx
                else:
                    answer[0] = min(answer[0], y_idx)

                if answer[1] == -1:
                    answer[1] = x_inx
                else:
                    answer[1] = min(answer[1], x_inx)

                answer[2] = max(answer[2], y_idx + 1)
                answer[3] = max(answer[3], x_inx + 1)
                    
    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/161989

배열의 타겟 요소를 길이m 안에 포함시키는 문제

한번에 최대한 많은 타겟 요소를 처리해야 한다

단위가 m이므로 한번 칠하고 그 다음 요소로 이동

길이가 벗어나면 어차피 칠해졌으니 종료

O(n/m). 리스트 길이 n, 단위 m. n은 클수록 오래걸리고 m은 작을수록 오래걸린다

```python
def solution(n, m, section):
    answer = 0
    painted = 0
    for part in section:
        if painted < part:
            answer += 1    
            painted = part + m - 1
    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/160586?language=python3

문자열과 카운트를 매핑하는 문제.

여러 문자열 리스트 중 최소값을 사전에 넣고 타겟을 계산한다.

먼저 한번씩 순회, 타겟 리스트 순회

O(n*m). keymap length * keymap[i] length

```python
def solution(keymap, targets):
    answer = []
    key_to_num_dict = defaultdict(int)
    
    for keys in keymap:
        for count, key in enumerate(keys, 1):
            if key_to_num_dict[key] == 0 or key_to_num_dict[key] > count:
                key_to_num_dict[key] = count

    for target in targets:
        count = 0
        for target_char in target:
            if not key_to_num_dict[target_char]:
                count = -1
                break
            count += key_to_num_dict[target_char]
        answer.append(count)

    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/159994

두 문자열 리스트에서 짝이 맞는 문자열 찾는 문제

두 리스트 중 하나라도 해당되면 통과. 바라보는 index + 1

중간에 제거하지 못하면 실패

O(n). goal이 길면 커진다.

```python
def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1_idx = cards2_idx = 0
    for goal_text in goal:
        if cards1_idx < len(cards1) and goal_text == cards1[cards1_idx]:
            cards1_idx += 1
            continue
        if cards2_idx < len(cards2) and goal_text == cards2[cards2_idx]:
            cards2_idx += 1
            continue

        return 'No'
    
    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/155652

조건에 맞춰 문자열 변환하는 문제

알파벳 리스트에서 skip을 미리 제거

z 넘어가면 a로 돌아가는 것도 주의. 나머지 구해서 인덱스로 사용한다

O(n). goal이 길면 커진다.

```python
def solution(s, skip, index):
    answer = ''
    skip_map = defaultdict(int)
    for skip_char in skip:
        skip_map[skip_char] = 1
    skiped_alphabet_list = [alpha for alpha in string.ascii_lowercase if not skip_map[alpha]]
    alphabet_to_idx_dict = defaultdict(int)
    for idx, alpha in enumerate(skiped_alphabet_list):
        alphabet_to_idx_dict[alpha] = idx

    for s_char in s:
        target_idx = alphabet_to_idx_dict[s_char] + index
        if len(skiped_alphabet_list) <= target_idx:
            target_idx = target_idx % len(skiped_alphabet_list)
        answer += skiped_alphabet_list[target_idx]

    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/147355

부분 배열과 타겟의 크기를 비교하는 문제

타겟 길이 만큼 부분배열 만드는 반복문으로 체크

타겟보다 크면 집계

O(n)

```python
def solution(t, p):
    p_len = len(p)
    answer = 0
    for i in range(p_len - 1, len(t)):
        start = i - (p_len - 1)
        if int(t[start:i + 1]) <= int(p):
            answer += 1
    return answer
```
---

https://school.programmers.co.kr/learn/courses/30/lessons/142086

동일한 문자가 어디에 있는지 찾는 문제

처음 등장이면 -1, 재등장은 얼마나 멀리 떨어져 있는지

사전으로 관리해서 없으면 첫등장. 인덱스 넣기

재등장이면 계산. 최신화.

O(n)

```python
def solution(s):
    answer = []
    char_to_idx_dict = {}
    for idx, s_char in enumerate(s):
        if not s_char in char_to_idx_dict:
            answer.append(-1)
            char_to_idx_dict[s_char] = idx
        else:
            answer.append(idx - char_to_idx_dict[s_char])
            char_to_idx_dict[s_char] = idx

    return answer
```
---
