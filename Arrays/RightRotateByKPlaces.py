'''
Question: Right Rotate the array by K places
TC: O(d + n - d + d) = O(N + D)
SC: O(d)
'''


def rightRotateByK(nums: list[int], k: int) -> list[int] :

    noOfShifts = k % len(nums)

    temp_array = []
    for i in range(len(nums) - noOfShifts, len(nums)):
        temp_array.append(nums[i])

    for i in range(len(nums)-1 , noOfShifts -1, -1): #decremental loop because increment == out of index, here think last becomes second last etc etc
        nums[i] = nums[i - noOfShifts]

    for i in range(len(temp_array)):
        nums[i] = temp_array[i]

    return nums

def main():
    array = [1, 2, 4, 7, 7, 5]
    k = 2
    answer = rightRotateByK(array, k)
    print(answer)
main()
