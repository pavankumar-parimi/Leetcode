def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    index = -1
    i = 0
    l = len(arr)

    while i < l:
        if arr[i] - x == 0:
            index = i
            break
        else:
            if i == 0 and arr[i] > x:
                index = i - 1
                break
            elif i + 1 < l and arr[i] < x < arr[i + 1]:
                index = i
                break
            elif i + 1 == l:
                if arr[i] > x:
                    index = i
                else:
                    index = l
        i += 1

    if index < 0:
        return arr[:k]
    elif index == l:
        return arr[-k:]
    else:
        Flag = False
        if arr[index] == x:
            i = index
            j = index + 1
        else:
            i = index
            j = index + 1
        l_c = 0
        r_c = 0
        ans = [0] * k

        while l_c + r_c < k:
            if arr[i] == x:
                l_c += 1
                i -= 1
            else:
                if i >= 0 and j < l and abs(arr[i] - x) <= abs(arr[j] - x):
                    l_c += 1
                    i -= 1
                else:
                    if i < 0:
                        r_c = k - l_c
                        break
                    elif j >= l:
                        l_c = k - r_c
                        break
                    r_c += 1
                    j += 1
        start = 0
        while l_c != 0:
            ans[start] = arr[index - l_c + 1]
            l_c -= 1
            start += 1

        i = 1
        while i <= r_c:
            ans[start] = arr[index + i]
            i += 1
            start += 1

        return ans
