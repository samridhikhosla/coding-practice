'''
Question: Remove duplicates on sorted array, without making copy of array, return number of unique elements
TC: O(N)
SC: O(1)
'''

def removeDuplicates(nums: list[int]) -> int : #O(2N) - creating a set takes O(N); converting it to a list takes O(N). TC, O(N) SC
    remDup = set(nums)
    total = len(nums)

    remDupList = list(remDup) #this doesn't preserve order so not okay
    return len(remDupList)

def removeDuplicatesOptimal(nums: list[int]) -> int :
    pointer_i = 0
    count = 1

    for pointer_j in range(1, len(nums)):
        if nums[pointer_i] != nums[pointer_j]:
            count += 1
            nums[pointer_i + 1] = nums[pointer_j]
            pointer_i = pointer_i + 1

    return count


def main():
    array = [1, 1, 2, 2, 2, 3, 3]
    answer1 = removeDuplicates(array)
    answer2 = removeDuplicatesOptimal(array)

    print(answer1)
    print(answer2)
main()
