class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        pref = []
        suff = []
        pp, sp = 1, 1

        for i in range(len(nums)):
            pref.append(pp)
            pp  *= nums[i]
        
        for j in range(len(nums) - 1, -1, -1):

            suff.insert(0, sp)
            sp *= nums[j]
        
        for i in range(len(pref)):
            result.append(pref[i] * suff[i])
        
        return result
        