#Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
#Hash Map/Table
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # stores {number: its index}
        
        for i, num in enumerate(nums):
            complement = target - num  # what number would I need to reach target?
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i  
