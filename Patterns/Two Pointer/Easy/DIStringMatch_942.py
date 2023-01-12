def diStringMatch(self, s: str) -> List[int]:
    i = 0
    s_l = len(s)
    j = s_l
    start = 0
    res = []

    while start < s_l:
        if s[start] == "D":
            res.append(j)
            j -= 1
        else:
            res.append(i)
            i += 1
        start += 1

    res.append(i)

    return res