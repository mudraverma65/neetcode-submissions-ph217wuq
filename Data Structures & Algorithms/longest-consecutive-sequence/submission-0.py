class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in num_set:
                current_streak = 1
                current_num = num

                while current_num+1 in num_set:
                    current_streak += 1
                    current_num += 1
                
                longest = max(current_streak, longest)
        return longest