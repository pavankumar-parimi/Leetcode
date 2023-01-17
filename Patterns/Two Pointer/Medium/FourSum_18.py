def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    l = len(nums)
    a = 0
    ans = []

    while a < l - 3:
        b = a + 1
        while b < l - 2:
            c = b + 1
            d = l - 1
            while c < d:
                if nums[c] + nums[d] == target - nums[a] - nums[b]:
                    if [nums[a], nums[b], nums[c], nums[d]] not in ans:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                    else:
                        c += 1
                        d -= 1
                elif nums[c] + nums[d] > target - nums[a] - nums[b]:
                    d -= 1
                else:
                    c += 1

            b += 1
        a += 1

    return ans