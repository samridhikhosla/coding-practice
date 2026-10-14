'''
Question: Find the missing number in an array
TC: O(N)
SC: O(1)
'''

def findMissingXOR(nums: list[int]) -> int :

    xor = len(nums) + 1 #because the array loops from 1 to n ie 0,1,2,3 (array has one less element)

    for i in range(len(nums)):
        xor ^= nums[i] ^ (i + 1)

    return xor


def findMissingSum(nums: list[int]) -> int :

    n = len(nums) + 1 #one element is missing, and we are trying to find the 'TOTAL'
    sum = (n * (n + 1))/2
    arr_sum = 0

    for i in range(len(nums)):
        arr_sum += nums[i]
  
    missing = int(sum - arr_sum)

    return missing

def findMissingBrute(nums: list[int]) -> int:
    for i in range(1, len(nums) + 1):
        if i not in nums:
            return i

def findMissingHash(nums: list[int]) -> int:
    arr = [0] * (len(nums) + 2)

    for num in nums:
        arr[num] = 1

    for i in range(1, len(arr)):
        if arr[i] == 0:
            return i

def main():

    array = [1,2,4,5]
    answer1 = findMissingXOR(array)
    print(answer1)
    answer2 = findMissingSum(array)
    print(answer2)
    answer3 = findMissingBrute(array)
    print(answer3)
    answer = findMissingHash(array)
    print(answer)

main()
