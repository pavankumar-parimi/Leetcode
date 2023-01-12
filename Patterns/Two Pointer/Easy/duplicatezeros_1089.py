def duplicateZeros(self, arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """

    """ Approach 1 """
    a_l = len(arr)
    i = 0
    j = a_l - 1

    while i < j:
        if arr[i] == 0:
            arr[j] = -1
            j -= 1
        i += 1

    start = -1

    while j >= 0:
        if i <= j or arr[j] != 0:
            arr[start] = arr[j]
            j -= 1
            start -= 1
        else:
            arr[start] = 0
            arr[start - 1] = 0
            start -= 2
            j -= 1