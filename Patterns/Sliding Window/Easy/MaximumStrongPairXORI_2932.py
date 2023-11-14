# def maximumStrongPairXor(self, nums: List[int]) -> int:
#     nums.sort()
#
#     max_xor_val = 0
#
#     start = 0
#     end = 1
#     nums_len = len(nums)
#
#     while start < nums_len:
#
#         if end >= nums_len:
#             start += 1
#             end = start + 1
#         else:
#             while (start + 1 < nums_len) and (nums[start] == nums[start + 1]):
#                 start += 1
#                 end = start + 1
#
#             if (start < nums_len) and (end < nums_len) and abs(nums[start] - nums[end]) <= nums[start]:
#                 if max_xor_val < (nums[start] ^ nums[end]):
#                     max_xor_val = nums[start] ^ nums[end]
#                     end += 1
#                     while end < nums_len and nums[end - 1] == nums[end]:
#                         end += 1
#                 else:
#                     end += 1
#             else:
#                 start += 1
#                 end = start + 1
#
#     return max_xor_val

# Approach 2 -- Using HashMap
def maximumStrongPairXor(nums):
    cache = list(set(nums))
    cache.sort()

    start = 0
    end = 1
    cache_len = len(cache)
    max_xor_val = 0

    while start < cache_len:
        if end >= cache_len:
            start += 1
            end = start + 1
        else:
            if abs(cache[start] - cache[end]) <= cache[start]:
                if max_xor_val < (cache[start] ^ cache[end]):
                    max_xor_val = cache[start] ^ cache[end]
                    end += 1
                else:
                    end += 1
            else:
                start += 1
                end = start + 1

    return max_xor_val


print(maximumStrongPairXor([1, 1, 2, 3, 5]))
