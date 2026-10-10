class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        complement number = target - current iteration
        
        '''

        my_dict = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if(complement not in my_dict):
                my_dict[nums[i]] = i
            else:
                return [my_dict[complement], i]
            