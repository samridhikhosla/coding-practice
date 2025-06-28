class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        if set(nums) == {0}:
            result_list = [0] * len(nums)
        else:
            result_list = [1] * len(nums)
            
            value = 1
            value_when_zero = 1
            counter = 0

            for i in range(len(nums)):

                if 0 in nums:
                    if nums[i] != 0:
                        value_when_zero = value_when_zero * nums[i]
                    else:
                        counter += 1
                        value = 0
                        
                        if counter > 1:
                            value_when_zero = 0
                else:
                    value *= nums[i]
            
            print(value_when_zero)
            
            for i in range(len(result_list)):
                result_list[i] *= value
            
            for i in range(len(nums)):
                if nums[i] == 0 :
                    result_list[i] = value_when_zero
                else:
                    result_list[i] = int(result_list[i] / nums[i])
        
        return result_list