class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            current_prod = 1
            for j in range(len(nums)):
                if i != j:
                    current_prod *= nums[j]
            result.append(current_prod)
        return result

        