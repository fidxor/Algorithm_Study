def topKFrequent(nums, k):
    numdict = dict()
    result = []
    
    for i in nums:
        if i in numdict:
            numdict[i] = numdict[i] + 1
        else:
            numdict[i] = 1

    numdict = sorted(numdict.items(), key = lambda x : x[1], reverse = True)

    for i in numdict[:k]:
        result.append(i[0])

    return result
        
topKFrequent([4, 5, 6, 3, 2, 2, 2, 3, 4, 5, 6, 1, 5,3, 2, 2, 23, 2,3, 4,5 ,2, 3, 4, 5, 6, 3], 3)