def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        # head에서 홀, 짝 자리를 정해준 후 두 칸씩 이동
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head
    return head
