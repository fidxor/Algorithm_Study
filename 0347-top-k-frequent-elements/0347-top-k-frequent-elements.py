class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numdict = dict()
        result = []

        # nums 배열 안에 있는 숫자의 키값이 있으면 value의 숫자를 올려주고 없으면 키로 추가 
        for i in nums:
            if i in numdict:
                numdict[i] = numdict[i] + 1
            else:
                numdict[i] = 1

        # value를 기준으로 정렬
        numdict = sorted(numdict.items(), key = lambda x : x[1], reverse = True)

        # 앞에서 부터 k개 리스트로 만들기
        for i in numdict[:k]:
            result.append(i[0])

        return result

        