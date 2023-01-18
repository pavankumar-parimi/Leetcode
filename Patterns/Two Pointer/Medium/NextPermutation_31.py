def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    res = -1
    l = len(nums)
    i = l - 2

    if l < 2:
        pass
    else:
        Flag = False
        while i > -1:
            j = l - 1
            k = j - 1
            while j > i:
                while k >= i:
                    if nums[k] >= nums[j]:
                        k -= 1
                    else:
                        nums[k], nums[j] = nums[j], nums[k]
                        nums[k + 1:] = nums[k + 1:][::-1]
                        Flag = True
                        break

                if Flag:
                    break
                j -= 1
                k = j - 1

            if Flag:
                break
            i -= 1

        if not Flag:
            i = 0
            j = l - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1