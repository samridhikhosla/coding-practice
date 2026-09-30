'''
Question: Left Rotate the array by K places
TC: O(noOfShifts + N - noOfShifts + noOfShifts)
SC: O(noOfShifts)
'''

def leftRotateByK(nums: list[int], k: int) -> list[int] :

    noOfShifts = k % len(nums)
    tempArray = []

    for i in range(noOfShifts):
        tempArray.append(nums[i])

    for i in range(noOfShifts, len(nums)):
        nums[i - noOfShifts] = nums[i]

    for i in range(len(tempArray)):
        nums[(len(nums) - noOfShifts) + i] = tempArray[i]

    return nums

def main():

    array = [1,2,3,4,5]
    k = 17
    answer = leftRotateByK(array, k)
    print(answer)

main()