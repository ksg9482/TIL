
김석규
오후 6:22 (3시간 전)
나에게

https://leetcode.com/problems/add-digits/description/?envType=problem-list-v2&envId=simulation&difficulty=EASY

숫자 각 자리를 별개 숫자로 인식해서 더하는 문제

한자리 수가 되면 반환 한다

33ms. Beats 76.68%

16.53MB. Beats 32.03%

O(n^2). 다중 반복문

```python
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = [int(digit) for digit in str(num)]
            num = sum(num)

        return num
```
---

https://leetcode.com/problems/fizz-buzz/?envType=problem-list-v2&envId=simulation&difficulty=EASY

숫자 맞춰서 특정 문자열을 리스트에 섞는 문제.

3으로 나눠진다, 5로 나눠진다, 3과 5 전부 나눠진다

처리하는 함수 만들고 리스트 컴프리헨션으로 하면 될 듯

43ms. Beats 53.92%

17.72MB. Beats 7.43%

O(n)

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [self.fizzBuzz_checker(data) for data in range(1, n + 1)]
       
        return ans

    def fizzBuzz_checker(self, digit):
        if digit % 15 == 0:
            return "FizzBuzz"
        elif digit % 3 == 0:
            return "Fizz"
        elif digit % 5 == 0:
            return "Buzz"
        else:
            return str(digit)
```
---

https://leetcode.com/problems/add-strings/description/?envType=problem-list-v2&envId=simulation&difficulty=EASY

굳이 전부 숫자로 바꿔놓지 않아도 됨. 몫과 나머지 구해서 넣는 방식으로 처리한다.

int로 직접 바꾸지 말라고 되어있긴 한데 실제로 않쓰면 성능이 지나치게 낮게 나왔다.

이 때는 {문자열:숫자} 사전을 만들고 자릿수를 곱해서 숫자를 만드는 방식을 사용했다.

35ms. Beats 88.92%

17.00MB. Beats 35.89%

O(n)

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == "0":
            return num2
        if num2 == "0":
            return num1
        
        result = []
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        
        while i >= 0 or j >= 0 or carry:
            digit_sum = carry
            
            if i >= 0:
                digit_sum += int(num1[i])
                i -= 1
            if j >= 0:
                digit_sum += int(num2[j])
                j -= 1
            
            result.append(str(digit_sum % 10))
            carry = digit_sum // 10
        
        return ''.join(result[::-1])
```
---
