class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} # val, number of times it appears
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1

        pairs = list(counter.items())
        sortedpairs = sorted(pairs, key = lambda p : p[1])


        ascendingvalue = []
        for topval in sortedpairs:
            ascendingvalue.append(topval[0])
        
        return ascendingvalue[-k:]


        