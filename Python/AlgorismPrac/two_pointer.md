https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

전형적인 투포인터 문제. 정석대로 포인터 2개로 풀어보자
for i 안에 for j를 둔다. for j는 i보다 1커서 항상 nums[i]보다 뒤를 바라본다
조건에 맞는 페어가 있으면 카운트를 올린다.

68ms. Beats 5.74%
16.64MB. Beats 11.84%

예상대로 성적이 안좋다. 2중 for문을 벗어나야 한다

O(n^2)

```python
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i, i_num in enumerate(nums):
            pointer = i + 1
            for j in range(pointer, len(nums)):
                if i_num + nums[j] < target:
                    count += 1
        return count
```

https://leetcode.com/problems/reverse-prefix-of-word/description/

포인터 하나는 0번을 가리킨다. 다른 하나는 +1 해가며 ch를 찾는다.
1. [0:ch]
2. [ch::]
두 배열을 만들고 문자열로 합친다

42ms. Beats 10.51%
16.43MB. Beats 90.11%

O(n). 슬라이싱으로 리스트를 만들고 join으로 새 문자열을 만드는 과정에서 소모가 너무 컷을까?

```python
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, word_ch in enumerate(word, 1):
            if word_ch == ch:
                start_to_ch = word[i-1::-1]
                ch_to_end = word[i::]
                return "".join([start_to_ch, ch_to_end])

        return word
```


https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

리스트에 문자열들이 있고, 그 문자열 중 첫번째 회문을 찾는 문제. -> 처음 회문이니 순서대로 가야한다.
문자열 리스트는 인덱스 안쓴다.
회문 탐색은 문자열의 맨 앞과 맨 뒤를 투 포인터로 비교한다. 만약 어긋나면 바로 다음 문자열로.
발견되면 반환하고 없으면 빈문자열을 반환한다.
start와 end가 교차하거나 거리가 1(len이 홀수. 가운데는 상관x)이라면 회문

108ms. Beats 5.11%
16.64MB. Beats 52.16%

O(n)? 근데 이속도면 아닌거 같다

```python
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            start = 0
            end = len(word) - 1
            flag = True
            while start < end:
                if word[start] == word[end]:
                    start += 1
                    end -= 1
                else:
                    flag = False
                    break
            if flag:
                return word

        return ""
```
