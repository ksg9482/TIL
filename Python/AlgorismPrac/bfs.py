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
