class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1

        min_val = inf
        while l<r:
            # if l==r:
            #     return nums[mid]
            mid = l + ((r-l)//2)
            print(l, r, mid)
            if nums[mid] > nums[r]:
                l = mid + 1 
            else:
                r = mid


        
        return nums[l]
