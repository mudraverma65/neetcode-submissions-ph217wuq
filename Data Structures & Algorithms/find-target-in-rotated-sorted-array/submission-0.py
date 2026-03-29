class Solution:

    def search(self, nums: List[int], target: int) -> int:
        
        return self.recursive(nums, 0, len(nums)-1, target)
    
    def recursive(self, nums: List[int], left : int, right: int, target: int) -> int:
        if left > right:
            return -1
        
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left]<=target<nums[mid]:
                return self.recursive(nums, left, mid-1, target)
            else:
                return self.recursive(nums, mid+1, right, target)
        else:
            if nums[mid]<target<=nums[right]:
                return self.recursive(nums, mid+1, right, target)
            else:
                return self.recursive(nums, left, mid-1, target)
            
