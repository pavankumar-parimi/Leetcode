def nextGreaterElement(self, n: int) -> int:
    res = -1
    lst = [char for char in str(n)]
    i = len(str(n)) - 2
    l = len(str(n))

    while i > -1:
        j = l - 1
        k = j - 1
        while i <= k:
            while i <= k:
                if int(lst[k]) >= int(lst[j]):
                    k -= 1
                else:
                    lst[k], lst[j] = lst[j], lst[k]
                    lst[k + 1:] = lst[k + 1:][::-1]
                    if int("".join(lst)) >= 2 ** 31:
                        return -1
                    return int("".join(lst))
            j = j - 1
            k = j - 1
        i -= 1

    return res