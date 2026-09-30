'''
Question: Left Rotate the array by one place
TC: O(N)
SC: O(1)
'''

def leftRotateByOne(nums: list[int]) -> list[int] :

    temp = nums[0]
    for i in range(1, len(nums)):
        nums[i-1] = nums[i]

    nums[len(nums)-1] = temp
    return nums

def main():

    array = [1,2,3,4,5]
    answer = leftRotateByOne(array)
    print(answer)

main()