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
