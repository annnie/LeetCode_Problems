class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for elem in range(len(nums)):
            goal = target - nums[elem]
            for item in range(len(nums)):
                if nums[item] == goal:
                    if(elem != item):
                        result = [elem, item]
                        return result
