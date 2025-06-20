def moveZeroes(self, nums):
    """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    non_zero_index = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

# Time complexity: O(n)
# Space complexity: O(1)
