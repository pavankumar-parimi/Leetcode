def captureForts(self, forts: List[int]) -> int:
    n_c = 0
    z_c = 0
    o_c = 0
    n_f = []
    p_f = []

    for index, each in enumerate(forts):
        if each == 0:
            z_c += 1
        elif each == -1:
            n_c += 1
            n_f.append(index)
        else:
            o_c += 1
            p_f.append(index)

    if n_c == 0 or o_c == 0 or z_c == 0:
        return 0

    m_f = 0
    i = 0
    j = 0

    while i < n_c and j < o_c:
        if n_f[i] < p_f[j]:
            if i + 1 < n_c and n_f[i + 1] < p_f[j]:
                i += 1
            else:
                m_f = max(m_f, p_f[j] - n_f[i])
                i += 1
        else:
            if j + 1 < o_c and p_f[j + 1] < n_f[i]:
                j += 1
            else:
                m_f = max(m_f, n_f[i] - p_f[j])
                j += 1

    return m_f - 1
