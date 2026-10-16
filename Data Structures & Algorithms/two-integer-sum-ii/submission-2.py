class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        go = 0
        back = len(numbers) - 1
        

        while go < back:
            added = numbers[go] + numbers[back]
            if added < target:
                go += 1
            elif added > target:
                back -= 1
            else:
                return [go+1, back+1]