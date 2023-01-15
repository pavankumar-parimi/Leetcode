def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    l = len(nums)
    res = []

    for i in range(l - 2):
        k = i + 1
        j = l - 1
        while k < j:
            b = -(nums[k] + nums[j])
            if nums[i] == b:
                if [nums[i], nums[k], nums[j]] not in res:
                    res.append([nums[i], nums[k], nums[j]])
                k += 1
                j -= 1
            elif nums[i] > b:
                j -= 1
            else:
                k += 1
    return res