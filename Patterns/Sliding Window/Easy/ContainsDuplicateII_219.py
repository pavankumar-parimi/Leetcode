def containsNearbyDuplicate1(nums, k):
    # Approach 1 Complexity --> O(N**2) Two Pointer Method

    nums_len = len(nums)

    start = 0
    end = start + 1

    while start < nums_len:
        if end >= nums_len:
            start += 1
            end  = start + 1
            continue

        if end-start <= k and nums[start] ==  nums[end]:
            return True
        elif end-start <= k and nums[start] != nums[end]:
            end = end + 1
        elif end-start > k:
            start += 1
            end = start + 1
    return False


def containsNearbyDuplicate2(nums, k):

    # Approach 2 Complexity --> O(N**2). Hashmap

    hash_map = {}

    for index, each in enumerate(nums):
        if each not in hash_map:
            hash_map[each] = [index]
        else:
            hash_map[each].append(index)

    for each, arr in hash_map.items():
        start = 0
        end = start + 1
        while end < len(arr):
            if arr[end]-arr[start] <= k:
                return True
            else:
                start += 1
                end = start + 1

    return False


def containsNearbyDuplicate3(nums, k):

    # Approach 3 HashMap where keys are elements and values are recent index of element

    hash_map = {}

    for index, each in enumerate(nums):
        if each not in hash_map:
            hash_map[each] = index
        elif index - hash_map[each] <= k:
            return True
        else:
            hash_map[each] = index
    return False

