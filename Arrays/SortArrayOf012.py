'''
Question: Sort an Array of 0s, 1s and 2s - Dutch National Flag
TC: O(N)
SC: O(1)
'''

'''
All zeroes : 0 to low - 1
All Ones : low to mid - 1
All Twos : high + 1 to n - 1

All unsort : mid to high
'''
def sort012(nums: list[int]) -> bool :

    low = 0
    mid = 0
    high = len(nums) - 1

    while (mid <= high):
        if nums[mid] == 0:
            temp = nums[low]
            nums[low] = nums[mid]
            nums[mid] = temp
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1
        else:
            temp = nums[high]
            nums[high] = nums[mid]
            nums[mid] = temp
            high -= 1

    return nums

def main():
    array = [1,1,1,1,0,0,0,0,2,2,2,1,0,2,0,1,1,0,2]
    answer = sort012(array)
    print(answer)
main()