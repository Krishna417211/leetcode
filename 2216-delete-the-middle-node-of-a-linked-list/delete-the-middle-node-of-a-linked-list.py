# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        slow = fast = head

        curr = head
        count = 0
        num = 0

        while fast and fast.next:
            slow = slow.next
            count  += 1
            fast = fast.next.next
        print(count)

        while curr and curr.next:
            num += 1

            if curr.next.val == slow.val and int(num) == count:
                curr.next = curr.next.next
                break
            curr = curr.next
        print(num)

        return head



