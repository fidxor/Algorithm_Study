import numpy as np

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        templist = []
        for y in range(len(arr1[i])):
            templist.append(arr1[i][y] + arr2[i][y])
        
        answer.append(templist)

    return answer