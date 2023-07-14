from itertools import combinations


def threeSum(nums: list[int]) -> list[list[int]]:
    lst = combinations(nums, 3)
    templst = []    

    for i in list(lst):
        if(sum(i) == 0):
            tmp = [*i]
            tmp.sort()
            templst.append(tmp)

    templst = set(templst)

    print(templst)
        

    return templst

threeSum([-1,0,1,2,-1,-4])
