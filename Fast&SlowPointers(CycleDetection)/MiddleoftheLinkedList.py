def middleNode(self, head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


# Time complexity: O(n)
# Space complexity: O(1)
