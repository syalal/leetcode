class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        while l<=r:
            mid = l + ((r-l)//2)
            mid_num = nums[mid]
            print(mid, mid_num)
            if target == mid_num:
                return mid
            elif target < mid_num:
                r = mid-1
            else:
                l = mid+1
            
        return -1


