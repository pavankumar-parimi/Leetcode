def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    res = 0
    arr2_len = len(arr2)
    for val1 in arr1:
        count = 0
        for val2 in arr2:
            if abs(val1 - val2) > d:
                count += 1
                continue
            else:
                break
        if count == arr2_len:
            res += 1
    return res