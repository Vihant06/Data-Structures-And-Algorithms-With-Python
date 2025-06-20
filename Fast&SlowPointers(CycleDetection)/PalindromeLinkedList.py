def isPalindrome(self, head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
# Time complexity: O(n)
# Space complexity: O(1)
