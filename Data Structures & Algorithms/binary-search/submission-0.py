class Solution:
    def search(self, nums: List[int], target: int, offset: int = 0) -> int:
        if len(nums) == 0:
            return -1
        begin = 0
        end = len(nums) - 1
        middle = begin + (end - begin) //2
        if nums[middle] == target:
            return middle + offset
        elif target > nums[middle]:
            return self.search(nums[middle+1:], target, offset + middle+1)
        elif target < nums[middle]:
            return self.search(nums[:middle], target, offset)
        

        