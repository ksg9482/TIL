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

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

트리의 깊이를 구하는 문제

한 층의 노드끼리 구분하는게 관건

한 층만 다루는 큐를 두어서 큐를 총 2개 사용한다

33ms. Beats 91.66%

17.57MB. Beats 65.70%

O(n).

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def bfs(root):
            q = deque([[root]])
            count = 0
            while q:
                node = q.popleft()
                inner_queue = deque()
                for i in node:
                    if i.left:
                        inner_queue.append(i.left)
                    if i.right:
                        inner_queue.append(i.right)
                if inner_queue:
                    q.append(inner_queue)
                count += 1
            return count
        return bfs(root)
```
---

https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

트리의 한 층 평균을 구하는 문제

한 층의 노드끼리 구분하는게 관건

층끼리 계산하고 결과에 넣는다

41ms. Beats 79.59%

18.52MB. Beats 12.53%

O(n).

```python
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def bfs(root):
            q = deque([[root]])
            averages = [root.val]
            while q:
                node = q.popleft()
                inner_queue = deque()
                for i in node:
                    if i.left:
                        inner_queue.append(i.left)
                    if i.right:
                        inner_queue.append(i.right)
                if inner_queue:
                    q.append(inner_queue)
                    list_len = len(inner_queue)
                    avr = sum([node.val for node in inner_queue]) / list_len
                    averages.append(avr)
            return averages
        return bfs(root)
```
---
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

한 층을 구성하는 children 끼리 묶는다

children이 몇이나 있는지 모르고, children의 children도 모른다

-> 더이상 children 없을 때까지 bfs

40ms. Beats 76.75%

18.18MB. Beats 9.07%

```python
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        def bfs(root):
            count = 1
            queue = deque([[root]])
            while queue:
                inner_queue = deque()
                node = queue.popleft()
                for i in node:
                    for child_node in i.children:
                        inner_queue.append(child_node)
                if inner_queue:
                    queue.append(inner_queue)
                    count += 1
            return count
        return bfs(root)
```
```

https://leetcode.com/problems/univalued-binary-tree/description/

root node를 기준으로 값 비교.

bfs로 순회하다 값 다르면 바로 false 반환

34ms. Beats 71.99%

16.50MB. Beats 16.27%

```python
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            queue = deque([root])
            root_val = root.val

            while queue:
                node = queue.popleft()
                if not (root_val == node.val):
                    return False
                
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)
            
            return True

        return bfs(root)
```
---

https://leetcode.com/problems/same-tree/description/

같은 값, 같은 모양의 트리인지 확인하는 문제

bfs로 순회하다 모양이나 값 다르면 바로 false 반환

p, q 짝지어서 동시에 움직이게 한다

34ms. Beats 65.72%

16.50MB. Beats 77.27%

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(p, q):
            queue = deque([[p, q]])
            while queue:
                node_p, node_q = queue.popleft()
                if not node_p and not node_q:
                    continue
                # 둘중 하나 없거나, 서로 다름
                if (not node_p or not node_q) or not (node_p.val == node_q.val):
                    print((not node_p or not node_q), node_p.val, node_q.val)
                    return False
                queue.extend([(node_p.left, node_q.left), (node_p.right, node_q.right)])
            return True
        
        return bfs(p, q)
```
https://leetcode.com/problems/same-tree/description/

시작점에서 네방향으로 bfs. 

유효범위 확인이 먼저.

조건이 맞으면 치환한다.

64ms. Beats 75.09%

16.56MB. Beats 85.73%

O(n*m) x, y축 연관

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        start_color = image[sr][sc]
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        queue = deque([(sr, sc)])

        while queue:
            current_r, current_c = queue.popleft()

            if current_r < 0 or current_c < 0 or current_r >= row or current_c >= col or image[current_r][current_c] == color  or image[current_r][current_c] != start_color:
                continue
            
            image[current_r][current_c] = color
            
            for i in directions:
                r, c = i
                queue.append(((current_r + r), (current_c + c)))
        
        return image
```
---

https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

두 요소를 더헤서 k를 만들수 있나 문제.

bfs를 이용한다. k에서 순회요소의 값을 뺀다 -> 사전에 넣어서 이후 해당하는 요소가 있나 검색.

값이 있으면 True 반환

52ms. Beats 90.86%

18.40MB. Beats 46.64%

O(n).

```python
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
            if root is None:
                return False
            
            q = deque([root])
            checked = defaultdict(bool)

            while q:
                node = q.popleft()
                
                if checked[node.val]:
                    return True
                
                checked[k - node.val] = True
                
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            return False
```

https://leetcode.com/problems/sum-of-left-leaves/description/

좌측 리프노드의 값을 더하는 문제.

맨 처음 root node는 구분해야 함. None이 왼쪽에 있으면 구분해야함. 

좌, 우가 번갈아가며 나오는걸 체크해야함

35ms. Beats 65.71%

16.96MB. Beats 23.30%

O(n).

```python
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
            if root.left is None and root.right is None:
                return 0

            q = deque([[root]])
            left_sum = 0
            
            while q:
                nodes = q.popleft()
                inner_q = deque()
                is_left = True

                for i, node in enumerate(nodes):
                    if node is None:
                        is_left = False
                        continue

                    if i%2 == 0:
                        is_left = True

                    if is_left and (node.left is None and node.right is None):
                        left_sum += node.val

                    inner_q.append(node.left)
                    inner_q.append(node.right)

                    is_left = False

                if inner_q:
                    q.append(inner_q)

            return left_sum
```
---
