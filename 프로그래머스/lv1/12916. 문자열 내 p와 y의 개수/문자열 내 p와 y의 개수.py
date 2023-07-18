def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    answer = s.lower().count("y") == s.lower().count("p")

    return answer