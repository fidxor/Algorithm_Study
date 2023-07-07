def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    index = 1    
    
    for i in citations:
        if i == index:
            answer = index
            break
        elif i < index:
            answer = index - 1
            break
        else:
             answer = index
                                
        index += 1
        
    return answer