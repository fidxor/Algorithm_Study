T = int(input())

def ValidPS(T):
    for i in range(T):
        bracket = input()
        printYesORNo(bracket)

    
def printYesORNo(bracket):
    lsttemp = []    

    for i in bracket:
        if not lsttemp:
            lsttemp.append(i)
             # 리스트에 첫번째 괄호가 ')' 이게 들어가면 for문 전부 돌거 없이 무조건 NO
            if i == ')':                
                break
            
            continue

        #리스트에 '(' 이게 쌓이다가 ')' 이게 들어가면 짝이 맞았기 때문에 맨 마지막에 들어간 '(' <- 괄호 제거
        #문자열 끝까지 검사했는데 괄호 한쪽이라도 남아있으면 NO, 리스트에 아무것도 없으면 YES
        if lsttemp[-1] == i:
            lsttemp.append(i)
        elif lsttemp[-1] != i:
            lsttemp.pop()        

    if not lsttemp:
        print("YES")
    else:
        print("NO")

ValidPS(T)