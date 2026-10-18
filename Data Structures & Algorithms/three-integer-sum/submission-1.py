class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
    

        finalset = set()
        #[-4 -1 -1 0 1 2]
        # i = 0, f = 1, b = 5
        for i in range(len(nums)-2):
            target = -nums[i]
            forw = i+1
            back = len(nums) - 1
            
            while forw < back:
                
                if nums[forw] + nums[back] < target:
                    forw += 1
                elif nums[forw] + nums[back] > target:
                    back -= 1
                else:
                    finalset.add((nums[i], nums[forw], nums[back]))
                    back -= 1

        finalist = list(finalset)
        return finalist