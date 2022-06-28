# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
#  It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(nums)
        target_element = 2

        for index in range(1, len(nums)):
            print(f'current nums: {nums}')
            if nums[index] <= nums[index - 1]:
                print(
                    f'This element needs to swap: index:{index}, value: {nums[index]}')
                for target in range(index+1, len(nums)):
                    if nums[target] > nums[index-1]:
                        print(
                            f'Found element to swap target index:{target}, value: {nums[target]}')
                        temp = nums[index]
                        nums[index] = nums[target]
                        nums[target] = temp
                        break
            print('. ')

        return nums


solution = Solution()
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
