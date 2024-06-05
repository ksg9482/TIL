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
