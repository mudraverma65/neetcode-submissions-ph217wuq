class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for number in nums:
            if number in duplicates:
                return True
                break
            else:
                duplicates[number] = 1
        return False

         