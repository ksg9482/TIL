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
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

가장 깊은 depth를 반환하는 문제. 

val이 None일때 카운트를 반환하게 한다. 단, None까지 포함하면 안되니 -1.

리스트에 넣고 최고값 구한다

37ms. Beats 76.08%

17.78MB. Beats 25.99%

O(n)

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(root, count = None, num_list=[]):
            if not count:
                count = 1
            else:
                count += 1
            if not root:
                num_list.append(count - 1)
                return count
            
            dfs(root.left, count, num_list)
            dfs(root.right, count, num_list)
            
            return num_list
        return max(dfs(root))
```

https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/

n-ary를 preorder하는 문제.

root, left -> right dfs하듯 하면 된다. 단, left, right가 아니라 배열 children으로 처리한다.

배열에 넣어서 반환한다.

44
ms
Beats 68.30%

18.22
MB
Beats 38.17%

O(n)

```python
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        def dfs(root, val_list=[]):
            if not root:
                return None
            
            val_list.append(root.val)

            for children in root.children:
                dfs(children, val_list)
            
            return val_list
            
        return dfs(root)
```
---
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/

이진트리를 순회하며 인진수로 계산하는 문제.

각 root의 val을 문자열로 더하고 leaf에서 리스트에 넣는다

리스트 값을 처리해서 반환

37ms. Beats 65.02%

16.84MB. Beats 6.32%

O(n)
```python
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root, digit=None, num_list=[]):
            if not digit:
                digit = ""

            if not root:
                return None
            
            digit += str(root.val)

            dfs(root.left, digit, num_list)
            dfs(root.right, digit, num_list)

            if not root.left and not root.right:
                num_list.append(digit)

            return num_list
        
        sum_num = 0
        ans = dfs(root)
        for num in ans:
            sum_num += int(num, 2)
        
        return sum_num
```
---

https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

트리의 레벨별 평균을 구하는 문제

레벨은 사전으로 관리하고, 재귀 한번 호출마다 인덱스+1 해서 레벨 구한다

사전은 합산, 개수를 넣어놓고 결과 반환할때 평균구하기. 

46ms. Beats 50.99%

18.56MB. Beats 12.34%

O(n)

```python
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #level:sum, count
        def dfs(root, level=None, level_to_val_dict={}):
            if not root:
                return None
            
            if not level:
                level = 1
            else:
                level += 1

            if not level_to_val_dict.get(level):
                level_to_val_dict[level] = {"sum":root.val,"count":1}
            else:
                level_to_val_dict[level]['sum'] += root.val
                level_to_val_dict[level]['count'] += 1

            if root.left or root.right:
                dfs(root.left, level, level_to_val_dict)
                dfs(root.right, level, level_to_val_dict)
            
            return level_to_val_dict
        
        ans = dfs(root)
        
        return [float(ans[data]['sum'] / ans[data]['count']) for data in ans]
```
---

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

children 없으면 리프노드. 여기까지 카운트 한다.

카운트를 배열에 넣고 -> 최대값 찾기

44ms. Beats 52.15%

18.14MB. Beats 7.92%

```python
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root, count=None, max_list=[]):
            if not root:
                return None
            
            if not count:
                count = 1
            else:
                count += 1

            if not root.children:
                max_list.append(count)
            else:
                for children in root.children:
                    dfs(children, count, max_list)

            return max_list
        
        if not root:
            return 0  
          
        ans = dfs(root=root)
        return max(ans)
```
---

https://leetcode.com/problems/binary-tree-postorder-traversal/description/

트리를 postorder로 순회하는 문제.

자식 -> 부모로 리스트에 삽입. 자식끼리는 left -> right순

32ms. Beats 75.81%

16.46MB. Beats 49.49%

```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, num_list=[]):
            if not root:
                return None

            dfs(root.left, num_list)
            dfs(root.right, num_list)

            num_list.append(root.val)

            return num_list
        
        if not root:
            return []
          
        ans = dfs(root=root)
        
        return ans
```
---

https://leetcode.com/problems/univalued-binary-tree/description/

트리의 모든 값이 동일한지 문제

루트를 기준으로 비교. 값이 다르면 False 반환.

not으로 잡으면 0도 포함됨. 0이 아니라 None임을 명시해야 함

27ms. Beats 95.51%

16.66MB. Beats 15.69%

```python
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, root_val=None):
            if not root:
                return True
            
            if root_val is None:
                root_val = root.val

            if not (root.val == root_val):
                return False
        
            left_result = dfs(root.left, root_val)
            right_result = dfs(root.right, root_val)

            return left_result and right_result
        
        return dfs(root)
```

https://leetcode.com/problems/binary-tree-preorder-traversal/description/

트리를 preorder로 순회하는 문제.

부모 -> 자식으로 리스트에 삽입.

30ms. Beats 86.50%

16.50MB. Beats 11.41%

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, num_list=[]):
            if not root:
                return None

            num_list.append(root.val)
            dfs(root.left, num_list)
            dfs(root.right, num_list)

            return num_list
        
        if not root:
            return []
          
        ans = dfs(root=root)
        
        return ans
```
---
https://leetcode.com/problems/leaf-similar-trees/description/

두 트리의 리프노드가 같은지 확인하는 문제

left, right 둘 다 없으면 리프노드 -> 이때만 배열에 넣는다.

배열 2개로 비교한다

* 같은 dfs함수로 했을때 기본값을 빈배열로 뒀을때 문제발생. 서로 다른 트리여도 dfs함수가 같으면 이미 기본값에 들어있음

33ms. Beats 77.96%

16.53MB. Beats 20.83%

```python
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root, num_list=None):
            if num_list is None:
                num_list = []

            if root is None:
                return None

            dfs(root.left, num_list)
            dfs(root.right, num_list)

            if root.left is None and root.right is None:
                num_list.append(root.val)
                
            return num_list
        
          
        root_1_list = dfs(root=root1)
        root_2_list = dfs(root=root2)
        
        return root_1_list == root_2_list
```
---

https://leetcode.com/problems/binary-tree-paths/description/

탐색 패스를 만드는 문제. val을 '->'로 잇는다

배열과 다음 노드로 전달될 문자열이 필요

넘어갈 때마다 문자열에 더하고 리프노드에서 배열에 넣는다

35ms. Beats 70.11%

16.56MB. Beats 25.13%

```python
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(root, path=None, num_list=None):
            if path is None:
                path = ""

            if num_list is None:
                num_list = []

            if root is None:
                return None

            if root.left is None and root.right is None:
                path += f"{root.val}"
                num_list.append(path)
            else:
                path += f"{root.val}->"

            dfs(root.left, path, num_list)
            dfs(root.right, path, num_list)

            return num_list
        
        return dfs(root=root)
```
---

https://leetcode.com/problems/same-tree/description/

두 트리를 비교하는 문제

부모 -> 좌 -> 우로 배열에 넣으면서 순회.

배열끼리 비교한다. 단, None이 포함되어야 순서를 알 수 있음. None이면 배열에 None을 넣는다

리프 이후로 넘어가지 않도록 좌, 우 다 있을 때만 재귀

26ms. Beats 96.38%

16.54MB. Beats 28.36%

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root, num_list=None):
            if num_list is None:
                num_list = []

            if root is None:
                num_list.append(None)
                return None

            num_list.append(root.val)

            if root.left is not None or root.right is not None:
                dfs(root.left, num_list)
                dfs(root.right, num_list)
                
            return num_list
        
        p_list = dfs(root=p)
        q_list = dfs(root=q)

        return p_list == q_list
```
---

https://leetcode.com/problems/binary-tree-tilt/description/

leaf노드 부터 감산해서 올라간다

바로 위 부모 노드는 좌, 우를 합쳐서 다시 반환

그 결과 값은 배열에 넣는 방식을 반복

연산이 끝난 리스트를 sum

49ms. Beats 52.44%

17.78MB. Beats 10.89%

```python
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        num_list = []
        def dfs(node):
            nonlocal num_list
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            num_calc = abs(left - right)
            num_list.append(num_calc)
            
            # 자식 노드의 값 합산과 val을 더해서 가져와야 함
            return node.val + left + right

        dfs(root)
        return sum(num_list)
```
