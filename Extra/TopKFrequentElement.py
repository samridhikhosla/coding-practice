class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for i in range(len(nums)):
            if(nums[i] not in freq_dict):
                freq_dict[nums[i]] = 1
            else:
                freq_dict[nums[i]] += 1
        
        sorted_dict = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
        
        flag = 0
        freq_list = []
        
        while flag < k:
            freq_list.append(sorted_dict[flag][0])
            flag += 1
        
        return freq_list