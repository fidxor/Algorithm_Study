def solution(n, lost, reserve):
    answer = 0

    lost.sort()
    reserve.sort()    

    lostcopy = lost.copy()

    for i in lost:
        # lost 와 reserve 에 같은 값이 있으면 제거
        if i in reserve:
            lostcopy.remove(i)
            reserve.remove(i)

    lostDuplicate = lostcopy.copy()

    for i in lostcopy:
        back = i - 1    # 잃어버린 학생 번호의 뒷번호
        forward = i + 1 # 잃어버린 학생 번호의 앞번호 

        # back 이나 forward 번호가 reserve 리스트에 있으면 
        # lost와 reserve에서 지워준다.
        if back in reserve:
            if i in lostDuplicate: lostDuplicate.remove(i)
            if back in reserve: reserve.remove(back)
        elif forward in reserve:
            if i in lostDuplicate: lostDuplicate.remove(i)
            if forward in reserve: reserve.remove(forward)

    # 총원에서 끝까지 체육복을 빌리지 못한 인원수를 빼준다.
    answer = n - len(lostDuplicate)

    return answer 