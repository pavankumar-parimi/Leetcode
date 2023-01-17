def compress(self, chars: List[str]) -> int:
    i = 0
    j = 0
    l = len(chars)
    tmp_str = ""

    while i < l:
        if chars[i] == chars[j]:
            i += 1
        else:
            if (i - j) > 1:
                tmp_str = tmp_str + chars[j] + str((i - j))
            else:
                tmp_str = tmp_str + chars[j]
            j = i

    if (i - j) > 1:
        tmp_str = tmp_str + chars[j] + str((i - j))
    else:
        tmp_str = tmp_str + chars[j]
    j = i

    t_l = len(tmp_str)

    for i in range(t_l):
        chars[i] = tmp_str[i]

    return t_l