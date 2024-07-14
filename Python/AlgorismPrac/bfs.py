https://leetcode.com/problems/island-perimeter/description/

첫번째 땅 찾기 -> 찾으면 bfs시작

땅의 네 방향 확인 -> 물, 밖이면 둘레 +1

땅 + 방문 안했으면 큐에 추가하고 방문 표시

417ms. Beats 44.68%

17.88MB. Beats 32.50%

O(n*m). x,y를 봐야 한다

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        # 4방향 설정. 
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        #bfs로 풀기
        def bfs(i, j, perimeter=None, visited=set()):
            if perimeter is None:
                perimeter = 0

            queue = deque([(i, j)])
            visited.add((i, j))

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions: # 동서남북으로 확인
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col: # 그리드 위치에 +1씩 해서 그리드 밖인지 안인지 확인
                        if grid[nx][ny] == 1: # 땅
                            if (nx, ny) not in visited: # 방문안한곳
                                queue.append((nx, ny))
                                visited.add((nx, ny))
                        else:
                            perimeter += 1 # 물 -> 둘레 추가
                    else:
                        perimeter += 1 #그리드 밖 -> 둘레추가
                    
            return perimeter

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1: # 가장 처음 시작할 땅 찾기
                    ans = bfs(i, j)
                    return ans
                    
        return 0
```
---
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/description/

클론 노드 찾기를 bfs로 처리.

dfs는 재귀로 left, right 호출해서 풀었지만 bfs로 할땐 queue에 넣어서 처리한다

루트의 left, right가 먼저 큐에 들어가고 다음은 그 자식 트리 순으로 큐에 넣어진다.

오리지널과 클론을 같은 타이밍에 넣어가며 순회하다가 조건 맞으면 클론을 반환.

293ms. Beats 91.95%

24.72MB. Beats 12.22%

O(n).

```python
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def bfs(original:TreeNode, cloned:TreeNode, target:TreeNode):
            ori_queue = deque([original])
            clone_queue = deque([cloned])

            while ori_queue:
                node = ori_queue.popleft()
                clone_node = clone_queue.popleft()
                if node:
                    if node == target:
                        return clone_node
                
                if node.left:
                    ori_queue.append(node.left)
                    clone_queue.append(clone_node.left)
                if node.right:
                    ori_queue.append(node.right)
                    clone_queue.append(clone_node.right)
        
        return bfs(original, cloned, target)
```
---
https://leetcode.com/problems/merge-two-binary-trees/description/

두 트리 병합 문제

bfs로 queue에 넣어서 처리

트리 두 개 동시에 순회 -> 반환하는 root1에 기준 맞춤

59ms. Beats 74.13%

16.83MB. Beats 76.40%

O(n).

```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1:
            return root2
        
        def bfs(root1:TreeNode, root2:TreeNode):
            queue = deque([(root1, root2)])

            while queue:
                t_1, t_2 = queue.popleft()

                if not t_1 or not t_2: # left, right 있어야 동작. 다음거 반복 전에 미리 처리 
                    continue

                t_1.val += t_2.val

                if not t_1.left: # 없으면 넣어야 함 -> None 가리켜서 그거 처리해야 함
                    t_1.left = t_2.left
                else:
                    queue.append((t_1.left, t_2.left))

                if not t_1.right: # 없으면 넣어야 함 -> None 가리켜서 그거 처리해야 함
                    t_1.right = t_2.right
                else:
                    queue.append((t_1.right, t_2.right))

            return root1
                
        return bfs(root1, root2)
```
https://leetcode.com/problems/invert-binary-tree/description/

트리를 뒤집는 문제

bfs로 큐에 넣는 방식으로 처리

작은 노드 자체는 left, right를 서로 교환하는 반복.

35ms. Beats 58.67%

16.57MB. Beats 14.84%

O(n).

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root):
            q = deque([root])
            while q:
                node = q.popleft()
                if node:
                    node.left, node.right = node.right, node.left
                # 먼저 좌, 우 바꾸고 큐에 삽입. 작은 노드 자체는 좌우만 바꾸면 된다
                    q.extend([node.left, node.right]) # extend로 좌우 한꺼번에 넣는게 편하다
            return root
        return bfs(root)
```
---
