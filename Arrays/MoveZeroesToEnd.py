'''
Question : Move zeroes to the end of the list.

TC: O(N + N)
SC: O(N)
'''

def moveZeroes(nums: list[int]):

    temp_arr = []

    for i in range(len(nums)):
        if nums[i] != 0:
            temp_arr.append(nums[i])

    rem_zeores = len(nums) - len(temp_arr)

    for i in range(rem_zeores):
        temp_arr.append(0) 

    return temp_arr
   

def main():
    x = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
    print(moveZeroes(x))
main()