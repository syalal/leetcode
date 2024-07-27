class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0 
        end = len(nums)-1
        i=0
        for j in range(-1, 1, -1):
            if nums[i] != val:
                end = nums[i]
                break
        while i <= end:
            if nums[i] == val:
                nums[i] = nums[end] 
                end -= 1
            else:
                i += 1
        return i
