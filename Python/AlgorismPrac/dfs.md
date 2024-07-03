https://leetcode.com/problems/range-sum-of-bst/description/

기본적인 DFS문제. 

None 처리는 0으로.

low 이상 high 이하 찾는 문제(동일 값 포함)

rangeSumBST 자체가 트리 탐색으로 기능.

low보다 낮으면 탐색 -> 재귀로 끝까지 찾는다

high보다 높으면 탐색 -> 마찬가지

102ms. Beats 89.22%

23.61MB. Beats 28.85%

```python
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
```
---
