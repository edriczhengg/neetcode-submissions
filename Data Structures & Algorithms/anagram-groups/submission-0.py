class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouping = {}
        for strings in strs:
            sortedstring = "".join(sorted(strings))
            if sortedstring in grouping:
                grouping[sortedstring].append(strings)
            else:
                grouping[sortedstring] = [strings]

        megalist = list(grouping.values())

        return megalist