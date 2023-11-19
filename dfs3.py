from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [0 for _ in range(len(words))]
    queue = deque()
    queue.append((begin, 0))
    
    while queue:
        current_word, count = queue.popleft()
        
        if current_word == target:
            return count
        
        for i in range(len(words)):
            diff_count = 0
            for j in range(len(current_word)):
                if words[i][j] != current_word[j] and visited[i] == 0:
                    diff_count+= 1
            
            if diff_count == 1 and visited[i] == 0:
                visited[i] = 1
                
                queue.append((words[i], count+1))  
                    
    return 0