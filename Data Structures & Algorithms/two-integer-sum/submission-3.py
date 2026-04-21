class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dif_map = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in dif_map:
                return [dif_map[dif], i]
            dif_map[nums[i]] = i