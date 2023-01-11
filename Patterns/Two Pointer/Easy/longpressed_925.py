def isLongPressedName(name: str, typed: str) -> bool:

    n_l = len(name)
    t_l = len(typed)

    if t_l < n_l:
        return False

    i = 0
    j = 0

    while i < n_l and j < t_l:

        if name[i] == typed[j]:
            i += 1
            j += 1
        else:
            return False

        while i < n_l and j < t_l and name[i] != typed[j] and name[i-1] == typed[j]:
            j += 1

    if i == n_l and j <= t_l:
        while j < t_l:
            if name[i-1] == typed[j]:
                j += 1
            else:
                return False
        return True
    else:
        return False


