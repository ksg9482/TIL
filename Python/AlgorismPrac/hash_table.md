https://leetcode.com/problems/number-of-good-pairs/
```python
"""
순회 할 때 이전 요소는 고려할 필요 없다.
내가 맨 처음 등장하면 딕셔너리에 값:카운트0으로 넣는다
같은 값이 있으면 그게 페어. 값이나 인덱스가 아니라 몇개인지

페어일 때 지금까지 몇번 나왔는지 결과값에 계속 더한다

순회 한번이니 O(n).
"""
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
