class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        checker = {}

        for n in range(len(nums)):
            checker[nums[n]] = n

        for k in range(len(nums)):
            diff = target - nums[k]
            if(diff in checker and k != checker[diff]):
                return [k, checker[diff]]
            
        
            