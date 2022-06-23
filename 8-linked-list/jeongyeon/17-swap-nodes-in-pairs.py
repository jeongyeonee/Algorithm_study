'''
값만 변경
Runtime: 41 ms
Memory: 13.9 MB
'''

def swapPairs_change_value(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head

    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head
