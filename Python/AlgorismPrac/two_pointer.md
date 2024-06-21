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

# ver.2
"""
word와 word 뒤집어서 바로 비교. 확실히 빨라졌다
79ms. Beats 46.55%   
16.70MB. Beats 14.70%
"""
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word

        return ""
```

https://leetcode.com/problems/flipping-an-image/description/

-1번 인덱스 요소부터 변환하고 리스트에 삽입. 
변환할 값은 사전으로 관리. if로 판단하고, 변경하는 것 보다 바로 참조하는 게 빠를 것 같다.
-> 실제로 시간복잡도 59ms. Beats 6.50%. 사전이 훨씬 빠르다

51ms. Beats 45.83%   
16.54MB. Beats 38.06%

O(n^2)
```python
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []

        convert_map = {
            1: 0,
            0: 1
        }
        for image_nums in image:
            flip_list = []
            for image_num in image_nums[::-1]: # 슬라이싱은 O(n)
                flip_list.append(convert_map[image_num])
            ans.append(flip_list)
        return ans
```

https://leetcode.com/problems/lexicographically-smallest-palindrome/description/

문자열의 맨 앞과 맨 뒤를 포인터로 잡고 비교하며 가운데로 모은다.
알파벳은 빌트인 이용.

112ms. Beats 58.68%   
16.66MB. Beats 71.19%


O(n). 리스트 길이의 반 연산 -> 리스트가 길수록 선형으로 늘어남

```python
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        alpha_dict = {alpha: i for i, alpha in enumerate(string.ascii_lowercase)}
        s_list = list(s)
        start = 0
        end = len(s) - 1   
        while start < end:
            if s_list[start] != s_list[end]:
                if alpha_dict[s_list[start]] > alpha_dict[s_list[end]]:
                    s_list[start] = s_list[end]
                else:
                    s_list[end] = s_list[start]
            
            if end - start <= 1:
                break

            start += 1
            end -= 1

        return "".join(s_list)
```

https://leetcode.com/problems/merge-strings-alternately/description/

word1과 word2 중 더 긴 길이로 반복문.
번갈아가면서 문자 더하기. 

1. 긴 길이로 해서 길이 안 넘게 계속 비교하기
2. 짧은 길이로 해서 더 남은 부분 한번에 더하기
뭐가 더 빠를까? 어차피 어떤 방법을 쓰든 순회는 끝까지 해야한다

31ms. Beats 81.57%   
16.33MB. Beats 97.59%


짧은 길이로 구하고 나머지 더하기 -> 38ms. Beats 37.33%
나머지 부분을 구하는 곳에서 리스트를 만드는 연산이 더 추가된다. 
불필요한 부분이 추가되기 때문에 더 안좋아진다.


O(n). 리스트 길이의 반 연산 -> 리스트가 길수록 선형으로 늘어남

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        longerst = word1_len if word1_len >= word2_len else word2_len

        ans = ""
        for i in range(longerst):
            if i <= word1_len - 1:
                ans += word1[i]

            if i <= word2_len - 1:
                ans += word2[i]

        return ans
```

https://leetcode.com/problems/middle-of-the-linked-list/description/

먼저 한 번 순회해서 총 길이 파악. 연결리스트는 거꾸로 찾아갈 수 없다.
길이의 반에 해당하는 노드 반환. 전체 연결리스트의 길이에 따라 반환하는 방식 달라짐.
홀수면 가운데, 짝수면 가운데 + 1

43ms. Beats 7.40%
16.44MB. Beats 67.74%

연결리스트는 일단 끝까지 순회해야 전체길이를 알 수 있는데 어떻게 풀어야 좋을까?

O(n). 끝까지 가는건 맞는것 같다. 투포인터를 활용하는 방법에 해결법이 있을듯 하다

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_len = 0
        node = head
        while node:
            head_len += 1
            node = node.next

        node = head # node 소모했으니 다시 채우기
        mid = head_len // 2 # 홀수면 올려서 +1한다
        for i in range(mid):
            node = node.next

        return node
```

https://leetcode.com/problems/sort-array-by-parity/description/

짝수 -> 홀수 순으로 정렬된 리스트를 반환하는 문제. 짝홀만 정렬하면 되고 차순정렬은 필요없음
단순하게 앞뒤로 포인터 잡고 서로 교환하자. 앞이 홀수면 앞 포인터 일시 정지. 뒤가 짝수면 뒤 포인터 일시정지.
서로 교환하는 식으로 반복.

68ms. Beats 53.50%
17.40MB. Beats 60.99%

O(n). 리스트가 커지면 연산도 선형으로 증가한다

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        while end > start:
            if not nums[start] % 2 == 0 and nums[end] % 2 == 0:
                nums[start], nums[end] = nums[end], nums[start]

            if nums[start] % 2 == 0:
                start += 1

            if not nums[end] % 2 == 0:
                end -= 1
            
        return nums
```

https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/

일단 정렬한다. [-9, -3, -1, 2, 3, 10]처럼 될 것. 연산했을 때 0이면 매칭.
nums[end] - nums[start] < 0 -> 더 작은 음수를 찾아야 한다. start + 1
nums[end] - nums[start] > 0 -> 더 작은 양수를 찾아야 한다. end - 1

103ms. Beats 77.47%
16.64MB. Beats 97.08%

O(nlogn). 정렬을 거치기 때문에 정렬 시간복잡도인 O(nlogn)이 적용.

```python
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        start = 0
        end = len(sorted_nums) - 1

        while end > start:
            if sorted_nums[end] + sorted_nums[start] == 0:
                return sorted_nums[end]
            elif sorted_nums[end] + sorted_nums[start] < 0:
                start += 1
            else:
                end -= 1

        return -1
```
