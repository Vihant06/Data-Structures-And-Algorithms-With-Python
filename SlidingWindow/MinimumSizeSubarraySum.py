def minSubArrayLen(self, target, nums):
    n = len(nums)
    l = 0
    sum = 0
    shortest = float('inf')
    k = 0

    for r in range(n):

        sum += nums[r]

        while sum >= target:
            shortest = min(shortest, r - l + 1)

            sum -= nums[l]
            l += 1

    return 0 if shortest == float('inf') else shortest
# Time complexity: O(n)
# Space complexity: O(1)
