class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevElement = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevElement:
                return[prevElement[diff], i]
            prevElement[n] = i 

        return