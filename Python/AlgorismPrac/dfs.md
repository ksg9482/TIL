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
https://leetcode.com/problems/increasing-order-search-tree/description/

val을 담은 리스트 -> 정렬 -> 순서대로 right에 담은 treenode 반환.
어차피 새 treenode의 right에만 값 들어감. none까지 고려할 필요 없음

21ms. Beats 99.65%

16.63MB. Beats 20.76%

O(nlogn)

```python
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def dfs(root: Optional[TreeNode], val_list:List = []):
            if not root:
                return None
            
            dfs(root.left, val_list)
            dfs(root.right, val_list)
            val_list.append(root.val)
            
            return val_list

        def list_to_tree(lst, index=0):
            if index < len(lst):
                node = TreeNode(lst[index])
                node.right = list_to_tree(lst, index + 1)
                return node
        
        val_list = dfs(root)
        val_list.sort()
        new_tree_node = list_to_tree(val_list)
        return new_tree_node
```
---

https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/

leaf부터 값 추출하는 문제.

값 추출보다 재귀를 먼저 넣어서 leaf를 먼저 리스트에 넣는다.

n-ary Tree 주의. 자식을 여러개 가질 수 있음 -> children을 순회하며 val를 뽑아내야 함

45ms. Beats 64.48%

18.32MB. Beats 10.75%

O(n). 정점수가 관건.

```python
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(root, val_list: List=[]):
            if not root:
                return None
            for root_val in root.children:
                dfs(root_val, val_list)
            val_list.append(root.val)

            return val_list
        return dfs(root)
```
---

https://leetcode.com/problems/invert-binary-tree/description/

트리노드를 뒤집는 문제.

순회하면서 left와 right를 반대로 삽입한다.

-> 재귀로 바로바로 생성.

34ms. Beats 68.00%

16.44MB. Beats 60.01%

O(n)

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root, invert_tree=None):
            if not root:
                return None
            invert_tree = TreeNode(root.val)
            invert_tree.left = dfs(root.right)
            invert_tree.right = dfs(root.left)
            return invert_tree
        return dfs(root)
```
---
https://leetcode.com/problems/binary-tree-inorder-traversal/description/

중위순회 하는 문제.

left -> root -> right 순으로 순회한다.

리스트는 순회하면서 바로 삽입. 

34ms. Beats 64.93%

16.64MB. Beats 11.63%

O(n)

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, val_list:List=[]):
            if not root:
                return None
            
            dfs(root.left, val_list)
            val_list.append(root.val)
            dfs(root.right, val_list)

            return val_list
        return dfs(root)
```
---
