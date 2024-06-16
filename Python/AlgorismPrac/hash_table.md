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


https://leetcode.com/problems/permutation-difference-between-two-strings/description/

문자key: 인덱스value
인덱스값끼리 비교해서 그 차를 계속 더한다.

47ms, Beats 6.95%.
16.44MB, Beats 84.10%

성적이 않좋다. 솔루션 전체가 기준이라면 더 빠른 언어로 작성된게 성적이 좋을것이고, 파이썬만 해당이라면 여기서 더 어떻게 향상시킬지 모르겠다
O(n).

```python
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_idx_dict = {}
        count = 0

        for i in range(len(s)):
            s_idx_dict[s[i]] = i
        
        for j in range(len(t)):
            diff = j - s_idx_dict[t[j]]
            count += abs(diff)

        return count
```

https://leetcode.com/problems/number-of-arithmetic-triplets/description/

숫자key: 인덱스value
diff를 더하면 값이 나오고 그 값이 딕셔너리의 키에 해당하면 nums에 있는거.
만약 diff 더한 값이 최고값보다 크면 arithmetic triplet을 구성할 수 없다. 거기서 break. 
내용이 아니라 카운트를 반환하는 것이니 카운트를 센다.

36ms, Beats 90.36%
16.50MB, Beats 41.99%

시간복잡도는 꽤 괜찮게 나왔다. 하지만 공간복잡도에서 아쉬움을 보인다. 
O(n).

```pythpn
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_idx_dict = {}
        nums_len = len(nums)
        maximum = 0
        count = 0

        for i in range(nums_len):
            nums_idx_dict[nums[i]] = i
            maximum = nums[i]

        for num in nums:
            diff_add_one = num + diff
            diff_add_two = num + (diff * 2)
            if diff_add_one > maximum or diff_add_two > maximum:
                break

            if nums_idx_dict.get(diff_add_one) != None and nums_idx_dict.get(diff_add_two) != None:
                count += 1
            
        return count
```

https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

알파벳이 적어도 하나씩 포함되는가 문제
1. 순회하면서 사전에 +1 한다
2. count를 두고 사전에 처음 넣는거면 count +1
3. 만약 count가 26이 되면 멈춰도 된다. 어차피 true

42ms. Beats 13.08%
16.44MB. Beats 80.98%


시간복잡도가 너무 낮다. 해시테이블이니 일단 딕셔너리 활용해서 풀었는데, set을 쓰면 더 빠를것 같다
O(n).

```python
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha_dict = {}
        alpha_num_limit = 26
        count = 0
        for alpha in sentence:
            if count >= alpha_num_limit:
                return True
            
            if alpha_dict.get(alpha) == None:
                alpha_dict[alpha] = 0
                count += 1
            else:
                alpha_dict[alpha] += 1
        
        return True if count >= alpha_num_limit else False
```

https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description/

2번 나오는 요소
XOR연산

순회하면서 각 요소가 몇번 나오나 확인. 그중 두 번 나온것만 연산

46ms. Beats 69.09%
16.36MB. Beats 93.94%

일반 더하기가 아님. 이거때문에 좀 해맸다. xor 함수로 하니까 됨. xor연산에 대해 더 알아봐야겠다
O(n).

```python
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        nums_dict = {}
        num_list = []
        for num in nums:
            if nums_dict.get(num) == None:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        
        for num in nums_dict:
            if nums_dict[num] == 2:
                num_list.append(num)
        
        return reduce(xor, num_list, 0)
```

https://leetcode.com/problems/find-maximum-number-of-string-pairs/description/

최대쌍 수 반환
사전에 넣어서 관리. {cd:0} -> 확인할 땐 dc로 리버스 해서 확인
페어가 몇개인지 찾는다. 시작은 0. 페어가 없으면 0을 반환.
각 문자열을 최대 한 쌍.

44ms. Beats 84.47%
16.44MB. Beats 78.10%

O(n).

```python
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        word_dict = {}
        for word in words:
            reversed_word = "".join(reversed(word))

            if word_dict.get(reversed_word) == None:
                word_dict[word] = 0
            else:
                word_dict[reversed_word] += 1

        pairs = word_dict.items()
        pair_count = 0
        for pair in pairs:
            pair_count += pair[1]

        return pair_count
```

https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/

부분배열을 다 합하는 문제
각 부분배열의 개별 개수의 제곱을 더한다.
[1] -> 1^2
[1,2,1] -> 1, 2 -> 2^2 : 요소는 3개지만 종류는 2개.

요소는 반드시 1개를 넘는다.(전체 빈배열 없음. 하위배열 빈배열 없음)

211ms. Beats 13.79%
16.50MB. Beats 55.84%

시간복잡도가 바닥이다. 배열을 이용했는데, 팩토리얼 구할 때 메모이제이션 하는 식으로 이 문제도 응용할 수 있지 않을까?

O(n^2). 부분배열을 구하는 과정에서 순회 안에서 재순회 한다.

```python
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        answer = 0
        count = 1 # 부분배열 안에서 처리
        for i in range(len(nums), 0, -1): # 전체에서 부분으로 줄여가는게 편함
            for j in range(i): # 부분 배열
                # 요소를 다 더하는게 아니라 종류 -> set
                subarray = list(set(nums[j: j + count]))
                answer += (len(subarray) ** 2)
            count += 1

        return answer
```
