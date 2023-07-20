class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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

        