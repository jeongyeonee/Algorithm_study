'''
13-palindrome--linked-list 참고
Runtime: 38 ms
Memory: 15.3  MB
'''

def reverseList_jy(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # empty head case
    if not head:
        return head

    rev = None
    while head:
        rev, rev.next, head = head, rev, head.next

    return rev

'''
재귀함수 이용
Runtime: 60  ms
Memory: 20.4 MB
'''

def reverseList_use_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # 현재노드와, 이전노드를 인수로 받는 reverse 함수
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)

'''
반복구조 이용
Runtime: 42 ms
Memory: 15.4 MB
'''

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # 현재노드와, 이전노드를 인수로 받는 reverse 함수
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)

