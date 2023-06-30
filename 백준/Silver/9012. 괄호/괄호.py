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
            if i == ')':                
                break
            
            continue

        if lsttemp[-1] == i:
            lsttemp.append(i)
        elif lsttemp[-1] != i:
            lsttemp.pop()        

    if not lsttemp:
        print("YES")
    else:
        print("NO")

ValidPS(T)