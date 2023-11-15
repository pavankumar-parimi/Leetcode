def minimumDifference(nums, k):
    # Approach 1 Sliding Window
    nums.sort()
    nums_len = len(nums)
    min_val = float('inf')

    for i in range(nums_len - k + 1):
        diff = nums[k + i - 1] - nums[i]
        if min_val > diff:
            min_val = diff

    return min_val


minimumDifference([9, 4, 1, 7])

