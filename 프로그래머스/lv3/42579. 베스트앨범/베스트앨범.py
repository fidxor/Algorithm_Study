def solution(genres, plays):
    answer = []

    songDict = dict()    

    # plays를 인덱스와 묶어서 리스트로 만든다   
    testlst = [(v, i) for i, v in enumerate(plays)]
     # output : [(500, 0), (600, 1), (150, 2), (800, 3), (2500, 4)]
    
    # plays와 인덱스를 묶은 리스트를 genres로 다시 묶어서 리스트를 만든다
    testlst = list(zip(genres, testlst))
    # output : [('classic', (500, 0)), ('pop', (600, 1)), ('classic', (150, 2)), ('classic', (800, 3)), ('pop', (2500, 4))]

    # 위에서 만든 리스트를 가지고 genres 값을 key로 잡아 dictionary를 만든다.    
    for i in range(len(genres)):       
        if testlst[i][0] in songDict:
            songDict[testlst[i][0]] += [testlst[i][1]]
        else:
            songDict[testlst[i][0]] = [testlst[i][1]]
    # output : {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]}
    
    # 각 key의 value로 들어있는 리스트에 plays만 더해줘서 리스트의 마지막에 넣어준다.    
    for i in songDict:
        temp = 0
        songDict[i].sort(key=lambda x: x[0], reverse=True) # 리스트 더해주기전에 plays 내림차순으로 정렬
        for j in songDict[i]:
            temp += j[0]            
        
        songDict[i] += list([temp])
    # output : {'classic': [(800, 3), (500, 0), (150, 2), 1450], 'pop': [(2500, 4), (600, 1), 3100]}

    
    # 리스트 마지막에 더해준 값을 기준으로 dictionary key를 정렬시켜준다
    songDict = dict(sorted(songDict.items(), key=lambda x : x[1][-1], reverse=True))

    # 결과 출력
    for i in songDict:
        if len(songDict[i]) > 2:
            for j in range(2):
                answer.append(songDict[i][j][1])
        else:
            answer.append(songDict[i][0][1])

    return answer