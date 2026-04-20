class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        numMap = {}
        i = 0

        for n in nums:
            if n in numMap:
                return True
            else:
                numMap[n] = i
                i=i+1

        return False
