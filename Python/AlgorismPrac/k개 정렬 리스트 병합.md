# k개 정렬 리스트 병합

### 입력 (k=3)   
[   
    1->4->5,   
    1->3->4,   
    2->6   
]   

### 출력   
1->1->2->3->4->4->5->6   
   
```python
def merge_k_lists(self, lists: list[ListNode]) -> ListNode:
    root = result = ListNode(None)
    heap = []

    #각 연결리스트의 루트를 힙에 저장
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    # 힙 추출 이후 다음 노드는 다시 저장
    while heap:
        # 파이썬의 heap모듈은 최소힙을 지원한다.
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        # k개의 연결리스트가 모두 힙에 들어있어야 가장 작은 노드가 차례댈 나올 수 있다. 
        # 그러므로 추출한 그 다음의 연결리스트의 노드를 다시 힙에 추가한다.
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))

    return root.next


```
