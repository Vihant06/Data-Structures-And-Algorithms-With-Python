def hasCycle(self, head):
    dummy = ListNode()
    dummy.next = head
    slow = fast = dummy
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            return True
    return False


# Time complexity: O(n)
# Space complexity: O(1)
