# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        min = 1
        max = n

        while max>=min:
            mid = (max+min) >> 1 

            num_check = guess(mid)

            if num_check==-1:
                max=mid-1
            elif num_check==1:
                min=mid+1
            elif num_check==0:
                return mid