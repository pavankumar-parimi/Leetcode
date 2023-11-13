def minimumRecolors(self, blocks: str, k: int) -> int:

    b_count = 0
    end = k - 1
    max_b = 0

    while end < len(blocks):
        if end == k - 1:
            for each in range(0, k):
                if blocks[each] == 'B':
                    b_count += 1
        else:
            if blocks[end] == 'B':
                b_count += 1
            if blocks[end - k] == 'B':
                b_count -= 1
        max_b = max(max_b, b_count)
        end += 1

    return k - max_b