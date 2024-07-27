class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def custom_sort(a, b):
            if a+b > b+a:
                return 1
            elif a+b < b+a:
                return -1
            else:
                return 0

        nums = [str(num) for num in nums]

        res_list = sorted(nums, key=cmp_to_key(custom_sort), reverse=True)
        res = ''.join(res_list).lstrip('0')
        if res != "":
            return res
        else:
            return "0"

        # def update_count(num):
        #     if num in num_count:
        #         num_count[num] += 1
        #     else:
        #         num_count[num] = 1

        # if len(nums) == 1:
        #     return nums[0]
        
        # num_count = {}
        # for num in nums:
        #     if num > 9:
        #         while num>0:
        #             r = num%10
        #             num = num//10
        #             update_count(r)
        #         continue

        #     update_count(num)

        # sorted_count = dict(sorted(num_count.items(), key= lambda x: x[1], reverse=True))
        # print(sorted_count)
        # power = sum(sorted_count.values()) - 1
        # res = 0
        # for k,v in sorted_count.items():
        #     for r in range(v):
        #         print(k, power)
        #         res += k*(10^power)
        #         power -= 1
        # return str(res)
            