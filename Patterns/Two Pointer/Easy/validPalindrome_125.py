def isPalindrome(self, s: str) -> bool:
    s_len = len(s)
    i = 0
    j = s_len - 1
    temp_sent = ""

    while i < j:
        while i < s_len and not s[i].isalnum():
            i += 1

        while j > 0 and not s[j].isalnum():
            j -= 1

        if i < s_len and j >= 0:

            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        else:
            break

    return True