https://leetcode.com/problems/number-of-good-pairs/

순회 할 때 이전 요소는 고려할 필요 없다.
내가 맨 처음 등장하면 딕셔너리에 값:카운트0으로 넣는다
같은 값이 있으면 그게 페어. 값이나 인덱스가 아니라 몇개인지

페어일 때 지금까지 몇번 나왔는지 결과값에 계속 더한다

순회 한번이니 O(n).

```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        pair_dict = {}
        for num in nums:
            if pair_dict.get(num) == None:
                pair_dict[num] = 1
            else:
                result += pair_dict[num]
                pair_dict[num] += 1
        

        return result
```


https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

nums[i]와 비교해서 더 작은 숫자가 몇개인지 배열 반환. 자기보다 앞 요소도 포함한다.
같은 수는 포함하지 않는다. 0을 요소로 한다.
순회하면서 비교. 포인터를 2개잡는다. i는 현재. j는 진행하며 순회.

부르트포스 -> O(n^2)

카테고리가 해시테이블이니 해시테이블을 이용해서 더 깔끔하게 푸는 방법이 있을것.
```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        nums_len = len(nums)

        for i in range(nums_len):
            count = 0
            for j in range(nums_len):
                if nums[i] > nums[j] and i != j:
                    count += 1
            ans.append(count)
        return ans
```


https://leetcode.com/problems/find-the-number-of-good-pairs-i/description/

페어 찾기. nums[i]를 nums[j] * k로 나눌수 있으면 페어. 이 페이가 몇개인지 반환.
나누어 떨어지는 페어를 찾아야함.

nums[i]가 1일 때 nums[j] * k가 1이면 페어. 1로 1을 나눌수 있음.
nums[i]가 3일 때 nums[j] * k가 4이면 페어가 아님. 4로 3을 딱 떨어지게 나눌수 없음.

방법1. 부르트포스. 계산한걸로 다 대조하면 됨
문제는 지나치게 큼. 10개씩만 되도 100번 연산함.

O(n^2)

그런데 중간쯤 간다. 63% beats. 이거 해시테이블로 풀려면 어떻게 해야할까?

```python
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        calc_nums2 = [num * k for num in nums2]
        count = 0
        for calc_num2 in calc_nums2:
            for num1 in nums1:
                if num1 % calc_num2 == 0:
                    count += 1
        return count   
```

https://leetcode.com/problems/unique-morse-code-words/description/

딕셔너리 2개를 만들자
1. 모스부호 -> {a:..}
2. 모스부호로 변환된 단어와 카운트 abc -> {..__..: 1}

중복 값 사전의 길이를 반환한다

-> O(n*k) ? 아니면 최악의 경우 요소의 각 길이가 요소 길이와 동일할 수 있으므로 O(n^2)?
-> 47ms, beats 7.91%. 16.65MB, beats 10.69%. 성적이 좋지 않음.


```python
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha_mos_dict = {
            "a": ".-",
	        "b": "-...",
	        "c": "-.-.",
	        "d": "-..",
	        "e": ".",
	        "f": "..-.",
	        "g": "--.",
	        "h": "....",
	        "i": "..",
	        "j": ".---",
	        "k": "-.-",
	        "l": ".-..",
	        "m": "--",
	        "n": "-.",
	        "o": "---",
	        "p": ".--.",
	        "q": "--.-",
	        "r": ".-.",
	        "s": "...",
	        "t": "-",
	        "u": "..-",
	        "v": "...-",
	        "w": ".--",
	        "x": "-..-",
	        "y": "-.--",
	        "z": "--.."
        }
        same_mos_dict = {}
        for word in words:
            mos = ""
            for alpha in word:
                mos += alpha_mos_dict[alpha]

            if same_mos_dict.get(mos) == None:
                same_mos_dict[mos] = 0
            else:
                same_mos_dict[mos] += 1
        return len(same_mos_dict)


https://leetcode.com/problems/decode-the-message/description/

문자와 암호문을 매핑하는 딕셔너리
알파벳을 순서대로 가지고있는 리스트
메시지를 순회하면서 중복이 아니면 문자와 암호문 딕셔너리에 넣는다
암호문 사전이 완성되면 실제 메시지를 암호문과 대조해 디코딩.

35ms, Beats 78.02%.
16.58MB, Beats 72.82%.
제법 괜찮게 나왔다.

O(n) -> key와 message중 더 긴 문자가 기준이 된다.

```python
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        secret_dict = {}
        alpha_count = 0
        decoded_message = ""
        for key_str in key:
            if key_str == " ":
                continue

            if secret_dict.get(key_str) == None:
                secret_dict[key_str] = alpha_list[alpha_count]
                alpha_count += 1
        
        for message_str in message:
            if message_str == " ":
                decoded_message += " "
            else:
                decoded_message += secret_dict[message_str]

        return decoded_message
```
