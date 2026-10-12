'''
Question : Move zeroes to the end of the list.

TC: O(2N)
SC: O(1)
'''

def moveZeroes(nums: list[int]):
    pointer_j = 0 #pointer for 0 in nums to swap
        
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pointer_j] = nums[i]
            pointer_j += 1

    for i in range(pointer_j, len(nums)):
        nums[i] = 0

    return nums
   

def main():
    x = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
    print(moveZeroes(x))
main()