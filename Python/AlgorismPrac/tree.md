https://leetcode.com/problems/find-mode-in-binary-search-tree/description/?envType=problem-list-v2&envId=tree&difficulty=EASY

트리 순회하면서 가장 많이 나온 수를 찾는 문제.

순회하면서 나온 수는 사전으로 관리.

수: 개수

dfs로 조회. 어차피 끝까지 다 봐야하면 이게 간단하다.

같은 개수라면 다 반환. 정렬하고 같은 수면 배열에 넣는다.

47ms Beats 58.27%

20.73MB Beats 5.55%

O(n)

```python
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: Optional[TreeNode], num_to_count_dict=defaultdict(int)):
            if root == None:
                return None
            
            num_to_count_dict[root.val] += 1
            dfs(root.left, num_to_count_dict)
            dfs(root.right, num_to_count_dict)

            return num_to_count_dict
        
        num_to_count_dict = dfs(root)

        sorted_val = sorted([(count, num_to_count_dict[count]) for count in num_to_count_dict], key=lambda a: a[1], reverse=True)
        largest_val = sorted_val[0][1]
        result = []
        for i in range(len(sorted_val)):
            if sorted_val[i][1] == largest_val:
                result.append(sorted_val[i][0])
            else:
                break

        return result
```
---

https://leetcode.com/problems/diameter-of-binary-tree/description/?envType=problem-list-v2&envId=tree&difficulty=EASY

트리 지름 찾는 문제. 두 노드를 연결했을 때 가장 긴 노드.

뎁스와 좌우 합계중 더 긴 쪽이 지름.

내부에서 찾고 바깥에서 이용해야 함 -> 리스트로 넣어서 참조타입으로.

가장 긴 값으로 반환 

38ms. Beats 95.72%

19.22MB. Beats 82.24%

O(n)


```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], length):
            if not root:
                return 0
            
            l_result = dfs(root.left, length)
            r_result = dfs(root.right, length)

            length[0] = max(length[0], l_result + r_result)

            return max(l_result, r_result) + 1
        
        length = [0]
        dfs(root, length)

        return length[0]
```
---

https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/?envType=problem-list-v2&envId=tree&difficulty=EASY

두번째로 작은 값 찾는 문제.

root는 좌우 값과 비교해서 작은 값이다 -> 맨처음 루트가 가장 작은 값.

다 같은 값이면 -1. 

29ms. Beats 88.93%

16.32MB. Beats 93.80%

O(nlogn). 정렬

```python
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def bfs(node, num_list=deque()):
            bfs_queue = deque([node])

            while bfs_queue:
                item = bfs_queue.popleft()
                num_list.append(item.val)
                if item.left:
                    bfs_queue.append(item.left)
                if item.right:
                    bfs_queue.append(item.right)
            
            return num_list
        
        result = bfs(root)
        result = sorted(result)
        for i in range(1, len(result)):
            if result[0] < result[i]:
                return result[i]
            
        return -1
```
---

https://leetcode.com/problems/search-in-a-binary-search-tree/description/?envType=problem-list-v2&envId=tree&difficulty=EASY

특정 노드를 찾는 문제.

해당 노드를 기준으로 한 서브 노드 트리를 반환한다

dfs로 찾는다.

53ms. Beats 71.39%

18.37MB. Beats 8.86%

O(n). 최악 노드 맨 끝에 있으면 끝까지 순회해야 함

```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root, val):
            if not root:
                return None
            
            if root.val == val:
                return root
            
            l = dfs(root.left, val)
            r = dfs(root.right, val)

            return l or r

        return dfs(root, val)
```
---
