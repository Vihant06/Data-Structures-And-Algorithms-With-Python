def findMaxAverage(self, nums, k):
    n = len(nums)
    cur_sum = 0
    for i in range(k):
        cur_sum += nums[i]
    max_average = cur_sum / k

    for i in range(n, k):
        cur_sum += nums[i]
        cur_sum -= nums[i - k]
        avg = cur_sum / k
        max_average = max(avg, max_average)
    return max_average
