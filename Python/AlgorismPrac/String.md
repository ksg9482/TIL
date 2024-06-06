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
