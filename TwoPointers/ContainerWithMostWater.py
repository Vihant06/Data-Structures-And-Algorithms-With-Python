def maxArea(self, height):
    """
        :type height: List[int]
        :rtype: int
        """
    lo = 0
    hi = len(height) - 1
    max_area = 0
    while lo < hi:
        w = hi - lo
        h = min(height[lo], height[hi])
        a = w * h
        max_area = max(max_area, a)
        if height[lo] < height[hi]:
            lo += 1
        else:
            hi -= 1
    return max_area
# Time complexity: O(n)
# Space complexity: O(1)
