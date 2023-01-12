def distinctAverages(self, nums: List[int]) -> int:
    nums.sort()
    avg = set()
    n_l = len(nums)
    i = 0
    j = n_l - 1

    while i < j:
        avg.add((nums[i] + nums[j]) / 2)
        i += 1
        j -= 1

    return len(avg)