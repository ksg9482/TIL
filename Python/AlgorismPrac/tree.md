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
