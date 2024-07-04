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
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/description/

original과 clone 두 트리가 있고 서로 동일한 요소를 바라보다가 target과 original이 같으면 그때 clone을 반환하는 문재

or로 요소가 있으면 그 요소 가져오게. 

맞는거면 요소, 아니면 None으로 or 연산이 계속 돌아가며 위로 올라옴. 

304ms. Beats 62.55%

24.44MB. Beats 79.70%

O(n)

```python

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # 일단 leaf 처리부터
        if not original:
            return None
        
        if original == target:
            return cloned
        
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
```
---

https://leetcode.com/problems/evaluate-boolean-binary-tree/description/

리프노드랑 줄기랑 따로 봐야한다 -> 리프노드가 T, F지만 이걸 판단하는 연산자는 val.

left, right가 None이 아니면 그냥 바로 T, F 반환하게 해서 연산자로 계산하자

42ms. Beats 83.17%

16.82MB. Beats 46.45%

O(n)

```python
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        0: False
        1: True
        2: OR
        3: AND
        """
        if root.val == 0 or root.val == 1:
            return root.val
        
        return self.evaluateTree(root.left) or self.evaluateTree(root.right) if root.val == 2 else self.evaluateTree(root.left) and self.evaluateTree(root.right)
```
---
https://leetcode.com/problems/evaluate-boolean-binary-tree/description/

val끼리 더해서 반환. 그거 받아서 노드 생성.

노드의 left, right에 넣으면서.

새 트리를 반환해야 함.

60ms. Beats 68.41%

16.85MB. Beats 78.72%

O(n)

```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1: Optional[TreeNode], root2: Optional[TreeNode], tree = None):
            
            if root1 and root2:
                tree = TreeNode(root1.val + root2.val)
                tree.left = dfs(root1.left, root2.left, tree)
                tree.right = dfs(root1.right, root2.right, tree)
                return tree
            else:
                if not root1 and root2:
                    tree = TreeNode(root2.val)
                    tree.left = dfs(None, root2.left, tree)
                    tree.right = dfs(None, root2.right, tree)
                    return tree
                
                if root1 and not root2:
                    tree = TreeNode(root1.val)
                    tree.left = dfs(root1.left, None, tree)
                    tree.right = dfs(root1.right, None, tree)
                    return tree

        return dfs(root1, root2)
```
---
