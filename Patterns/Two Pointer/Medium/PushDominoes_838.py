def pushDominoes(self, dominoes: str) -> str:
    l = len(dominoes)
    i = 0
    j = i
    ans = ""
    s_lst = [char for char in dominoes]

    while i < l:
        if dominoes[i] != ".":
            j = i
            break
        i += 1
    if i < l and dominoes[i] == "L":
        while i >= 0:
            s_lst[i] = "L"
            i -= 1

    i = j + 1
    while i < l:

        if dominoes[i] == ".":
            i += 1
            continue
        else:
            if dominoes[j] == "L" and dominoes[i] == "R":
                while j < i:
                    s_lst[j] = dominoes[j]
                    j += 1
                j = i
                i += 1
            elif dominoes[j] == "R" and dominoes[i] == "L":
                pos_i = i
                pos_j = j
                while pos_j + 1 <= pos_i:
                    Flag1 = False
                    Flag2 = False
                    if s_lst[pos_j + 1] == "." and s_lst[pos_j + 2] == ".":
                        Flag1 = True
                    if s_lst[pos_i - 1] == "." and s_lst[pos_i - 2] == ".":
                        Flag2 = True

                    if Flag1 and Flag2:
                        s_lst[pos_j + 1] = s_lst[pos_j]
                        s_lst[pos_i - 1] = s_lst[pos_i]
                    else:
                        break
                    pos_j = pos_j + 1
                    pos_i = pos_i - 1
                j = i
                i += 1
            elif dominoes[j] == "L" and dominoes[i] == "L":
                while j < i:
                    s_lst[j] = "L"
                    j += 1
                j = i
                i += 1
            elif dominoes[j] == "R" and dominoes[i] == "R":
                while j < i:
                    s_lst[j] = "R"
                    j += 1
                j = i
                i += 1

    if dominoes[j] == "R":
        while j < l:
            s_lst[j] = "R"
            j += 1

    return "".join(s_lst)
