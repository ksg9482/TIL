```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
            # 1. ans[i] == nums[i] 2. ans[i + n] == nums[i]
            # -> 같은 배열이 같은 순서로 반복되어야 한다
            ans = nums * 2
            return ans
```

```python
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # 부분배열 만큼 계속 더한다
        # 배열이 더 큰 수가 아니면 부분배열 초기화
        # 기존 maximum과 합 비교
        # 더 큰 수로 변경한다.
        maximum = 0
        sum_array = 0
        prev = 0

…            prev = num
    
        # 맨 마지막 요소도 비교진행
        if maximum < sum_array:
            maximum = sum_array
        
        return maximum
```

```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0

        for account_list in accounts:
            sum_value = sum(account_list)
            
            if maximum < sum_value:
                maximum = sum_value

        return maximum
```
