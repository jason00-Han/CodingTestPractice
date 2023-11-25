def solution(brown, yellow):
    answer = []
    total = brown + yellow

    for i in range(1, int(total**(1/2)) + 1):
        if total % i == 0:
            if 2 * (i + total // i - 2) == brown:
                return [max(i, total // i), min(i, total // i)]
                
    return answer
