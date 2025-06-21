class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        a_dict = {}
        for i in range(len(nums)):
            a_dict[i] = 1
            for j in range(len(nums)):
                if (i != j):
                    a_dict[i] = a_dict[i] * nums[j]
        
        a_list = []
        for j in a_dict.values():
            a_list.append(j)
        
        return a_list