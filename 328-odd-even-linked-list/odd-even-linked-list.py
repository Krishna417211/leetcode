class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:

        if not head:
            return None

        count = 0
        curr = head

        dummy1 = ListNode(0)
        even = dummy1

        dummy2 = ListNode(0)
        odd = dummy2

        while curr:
            if count == 0:
                even.next = curr
                even = even.next
                count = 1
            else:
                odd.next = curr
                odd = odd.next
                count = 0

            curr = curr.next

        odd.next = None
        even.next = dummy2.next

        return dummy1.next