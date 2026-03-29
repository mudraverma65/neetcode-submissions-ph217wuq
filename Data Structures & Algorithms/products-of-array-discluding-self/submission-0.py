class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_arr = [0] * len(nums)

        for i in range (0, len(nums)):
            prod = 1
            for j in range(0, len(nums)):
                if i != j:
                    prod = prod * nums[j]
            prod_arr[i] = prod
        return prod_arr


        