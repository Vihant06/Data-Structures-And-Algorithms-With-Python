def trap(self, height: List[int]) -> int:

    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    result = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            result += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            result += rightMax - height[r]

    return result
# Time complexity: O(n)
# Space complexity: O(1)
