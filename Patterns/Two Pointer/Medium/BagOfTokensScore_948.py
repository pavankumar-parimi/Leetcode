def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
    tokens.sort()
    score = 0
    i = 0
    l = len(tokens)
    j = l - 1

    while i <= j:
        if power >= tokens[i]:
            score += 1
            power -= tokens[i]
            i += 1
        elif tokens[j] > tokens[i] and score > 0:
            score -= 1
            power += tokens[j]
            j -= 1
        else:
            break
    return score