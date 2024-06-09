https://leetcode.com/problems/roman-to-integer/submissions/1277907779/

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value_map = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

        result = 0
        s_length = len(s)
        jump = False
        for i in range(s_length): #O(n)
            if jump:
                jump = False
                continue

            num = 0
            s_symbol = s[i]
            next_symbol = ""
            
            if i + 1 < s_length:
                next_symbol = s[i + 1]
            
            if s_symbol == "I" and next_symbol == "V":
                num = 4
                jump = True
            elif s_symbol == "I" and next_symbol == "X":
                num = 9
                jump = True
            elif s_symbol == "X" and next_symbol == "L":
                num = 40
                jump = True
            elif s_symbol == "X" and next_symbol == "C":
                num = 90
                jump = True
            elif s_symbol == "C" and next_symbol == "D":
                num = 400
                jump = True
            elif s_symbol == "C" and next_symbol == "M":
                num = 900
                jump = True
            else:
                num = symbol_value_map[s_symbol] #dict 접근: O(1)
            next_symbol = s_symbol

            result += num
        # O(n) 시간복잡도
        return result
```        

https://leetcode.com/problems/longest-common-prefix/submissions/1278416458/

```python
# 시간복잡도 개선 필ㅇㅅ
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        head = strs[0]
        is_break = False
        
        for i in range(len(head)):
            for word in strs:
                if (i >= len(word)) or (head[i] != word[i]):
                    is_break = True
                    break

            if is_break:
                break

            result.append(head[i])
            
        return "".join(result)
```

https://leetcode.com/problems/valid-parentheses/submissions/1278489272/

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        length = len(s)

        if (length == 0) or (length % 2 != 0):
            return False

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(")")
            elif s[i] == "[":
                stack.append("]")
            elif s[i] == "{":
                stack.append("}")
            elif len(stack) > 0 and stack[-1] == s[i]:
                stack.pop()
            else:
                return False
        
        if len(stack) != 0:
            return False

        return True
```

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)

        if haystack_len < needle_len:
            return -1
        
        for i in range(haystack_len):
            if needle == haystack[i:i+needle_len]:
                return i
        
        return -1
```

https://leetcode.com/problems/add-binary/submissions/1279023853/

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        1. a 바이너리 더하기
        2. b 바이너리 더하기
        3. 계산
        4. 결과값 바이너리 변환
        """
        a_value = 0
        b_value = 0
        value_list = [1]
        for i in range(len(a)-1, -1, -1):
            if len(value_list) <= (len(a)-1)-i:
                value_list.append(value_list[-1] * 2)

            if a[i] == "1":
                a_value += value_list[(len(a)-1)-i]

        for i in range(len(b)-1, -1, -1):
            if len(value_list) <= (len(b)-1)-i:
                value_list.append(value_list[-1] * 2)

            if b[i] == "1":
                b_value += value_list[(len(b)-1)-i]

        value_sum = a_value + b_value
        result_list = []
        is_run = True
        while is_run:
            if value_sum == 0:
                break
            div = divmod(value_sum, 2)
            value_sum = div[0]
            result_list.append(str(div[1]))

        result_list.reverse()
        return "".join(result_list) if result_list else "0" 
```

https://leetcode.com/problems/valid-palindrome/

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. lowercase 변환, 특수문자 및 공백 제거
          * 대소문자는 미리 변환이 좋을까 아니면 비교때 변환이 좋을까?
        2. 문자열 반 나눠서 스택에 넣기
          * 만약 홀수면 가운데는 필요없음.
        3. 스택에서 하나씩 빼며 비교
        """
        if len(s) == 1:
            return True
        
        only_str = re.sub(r"[^A-Za-z0-9]","", s).lower()
        mid = len(only_str) // 2
        left = list(only_str[0:mid])
        right = list(only_str[mid if len(only_str) % 2 == 0 else (mid + 1)::])

        for i in range(len(left)):
            word = left.pop()
            if word != right[i]:
                return False

        return True
```

https://leetcode.com/problems/valid-palindrome/description/

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        mid = end // 2 # 나머지가 있어도 int되서 잘림. 어차피 range 넘어가면 종료.
        for i in range(mid + 1): # mid로 반 나눈 값을 써도 s가 길면 선형으로 늘어난다.
            if start == end or start > end:
                break
            s[start], s[end] = s[end], s[start] # 튜플 패킹과 언패킹으로 동작한다고?
            start += 1
            end -= 1
    # O(n) 시간복잡도. O(1)이 불가능한 이유? 모든 문자열을 뒤집으려면 모든 문자열에 접근해야 함.
```

https://leetcode.com/problems/isomorphic-strings/description/

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 1 and s != t:
            return False
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            # 글자를 dict에 넣는다.
            if s_dict.get(s[i]) == None:
                s_dict[s[i]] = t[i]
                t_dict[t[i]] = s[i]
            
            # 이미 있는 글자면 값 확인. 같은 순서, 같은 형식 아니면 False
            if s_dict[s[i]] != t[i]:
                return False
        if len(s_dict) != len(t_dict): # 등장 문자 수가 같아야 한다.
            return False

        return True
```

https://leetcode.com/problems/valid-anagram/description/

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        for key in s_dict:
            # anagram이면 dict의 key가 동일해야 하고, 내용도 동일해야 함.
            if key not in t_dict or s_dict[key] != t_dict[key]:
                return False
            
        return True
```

https://leetcode.com/problems/word-pattern/description/

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splited_s = s.split(" ")
        pattern_len = len(pattern)
        pattern_dict = {}
        s_dict = {}

        if pattern_len != len(splited_s):
            return False
        
        for i in range(pattern_len):
            if pattern_dict.get(pattern[i]) == None:
                pattern_dict[pattern[i]] = splited_s[i]
                s_dict[splited_s[i]] = pattern[i]
            else:
                if pattern_dict[pattern[i]] != splited_s[i]:
                    return False

        if len(pattern_dict) != len(s_dict):
            return False
        
        return True
```

https://leetcode.com/problems/reverse-vowels-of-a-string/description/

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1
        vowel_dict = {
            "a":"a", "e":"e", "i":"i", "o":"o", "u":"u", 
            "A":"A", "E":"E", "I":"I", "O":"O", "U":"U", 
        }
        s_list = list(s)
        for i in range(end + 1):

```

https://leetcode.com/problems/first-unique-character-in-a-string/description/

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_num_dict = {}

        for i in range(len(s)):
            if s_num_dict.get(s[i]) == None:
                s_num_dict[s[i]] = {"idx": i, "count": 1}
            else:
                s_num_dict[s[i]]['count'] += 1

        for data in list(s_num_dict.items()):
            if data[1]['count'] == 1:
                return data[1]['idx']
            
        return -1
```

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        if s == " ":
            return s
        
        s_list = s.split(" ")
        ans = []
        for text in s_list:
            reverse_list = []
            for i in range(len(text) - 1, -1, -1):
                reverse_list.append(text[i])
            ans.append("".join(reverse_list))
        return " ".join(ans)
```

https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

```python
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        text_dict = {}
        common_text_dict = {}
        for i in range(len(list1)):
            text_dict[list1[i]] = i
                
        for i in range(len(list2)):
            common_text_val = text_dict.get(list2[i])
            if common_text_val != None:
                common_text_dict[list2[i]] = common_text_val + i

        items = list(common_text_dict.items())
        
        sorted_list = sorted(items, key=lambda x: x[1])

        target_num = sorted_list[0][1]
        ans = list(filter(lambda x: x[1] == target_num, sorted_list))

        return [text[0] for text in ans]
```
