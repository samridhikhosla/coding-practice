class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.binary_search(0, len(nums)-1, nums, target)


    def binary_search(self, low: int, high: int, nums: list[int], target: int) -> int:
        mid = (low + high) // 2

        if(low <= high):

            if(nums[mid] == target):
                return mid

            elif(nums[mid] < target):
                return self.binary_search(mid + 1, high ,nums, target)

            else:
                return self.binary_search(low, mid - 1 ,nums, target)
        
        else:
            return -1