class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq_list = [[] for i in range(0, len(nums)+1)]
        for num, freq in count.items():
            freq_list[freq].append(num)

        res = []
        for idx in range(len(freq_list)-1, 0, -1):
            print(freq_list[idx])
            for num in freq_list[idx]:
                res.append(num)
                if len(res) == k:
                    return res



