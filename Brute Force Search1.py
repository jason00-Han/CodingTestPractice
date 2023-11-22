def solution(answers):
    number_one = [1, 2, 3, 4, 5]
    number_two = [2, 1, 2, 3, 2, 4, 2, 5]
    number_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    number_one_count = 0
    number_two_count = 0
    number_three_count = 0
    
    # 각 학생이 정답을 맞춘 개수를 카운트
    for i in range(len(answers)):
        if answers[i] == number_one[i % len(number_one)]:
            number_one_count += 1
        if answers[i] == number_two[i % len(number_two)]:
            number_two_count += 1
        if answers[i] == number_three[i % len(number_three)]:
            number_three_count += 1
    
    max_count = max(number_one_count, number_two_count, number_three_count)
    answer = []
    
    # 가장 많은 문제를 맞힌 학생들을 리스트에 추가
    if max_count == number_one_count:
        answer.append(1)
    if max_count == number_two_count:
        answer.append(2)
    if max_count == number_three_count:
        answer.append(3)
    
    return answer
