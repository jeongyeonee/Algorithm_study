def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        # 홀, 짝 상태에서 두 칸씩 이동
        odd.next, even.next = odd.next.next, even.next.next
        # 왜 현재 포인트를..왜...한 칸...왜..?
        odd, even = odd.next, even.next

    odd.next = even_head
    return head
