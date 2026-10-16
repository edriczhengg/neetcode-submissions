class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1;

        sortedcounter = sorted(counter, key = counter.get, reverse = True)
        

        return sortedcounter[:k]
        