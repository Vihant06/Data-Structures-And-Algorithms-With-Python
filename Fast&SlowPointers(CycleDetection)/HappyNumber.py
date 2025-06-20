def isHappy(self, n):
    def getNext(n):
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit * digit
            n //= 10
        return sum
    slow = n
    fast = getNext(n)
    while fast != 1 and slow != fast:
        slow = getNext(slow)
        fast = getNext(getNext(fast))
    return fast == 1


# Time complexity: O(n)
# Space complexity: O(1)
