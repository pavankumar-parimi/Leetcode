def divisorSubstrings(self, num: int, k: int) -> int:
    count = 0

    str_num = str(num)
    str_num_len = len(str_num)

    for each in range(0, str_num_len - k + 1):
        if int(str_num[each:each + k]) != 0 and num % int(str_num[each:each + k]) == 0:
            count += 1

    return count