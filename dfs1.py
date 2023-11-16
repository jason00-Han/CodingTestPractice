def solution(numbers, target):
    leaves = [0]
    count = 0
    
    for num in numbers:
        temp = []
        for leaf in leaves:
            temp.append(leaf + num)
            temp.append(leaf - num)
        leaves = temp
        
        if target in leaves:
            count += 1
    return count

print(solution([1, 1, 1, 1, 1], 3))
