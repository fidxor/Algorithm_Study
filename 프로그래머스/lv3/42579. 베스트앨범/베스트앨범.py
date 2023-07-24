def solution(genres, plays):
    answer = []

    songDict = dict()    

    testlst = [(v, i) for i, v in enumerate(plays)]    
    
    testlst = list(zip(genres, testlst))     

    for i in range(len(genres)):       
        if testlst[i][0] in songDict:
            songDict[testlst[i][0]] += [testlst[i][1]]
        else:
            songDict[testlst[i][0]] = [testlst[i][1]]
    
    for i in songDict:
        temp = 0
        songDict[i].sort(key=lambda x: x[0], reverse=True)
        for j in songDict[i]:
            temp += j[0]            
        
        songDict[i] += list([temp])

    print(songDict.items())        

    songDict = dict(sorted(songDict.items(), key=lambda x : x[1][-1], reverse=True))

    for i in songDict:
        if len(songDict[i]) > 2:
            for j in range(2):
                answer.append(songDict[i][j][1])
        else:
            answer.append(songDict[i][0][1])

    print(answer)

    return answer