'''
Question: Check if the array is sorted
TC: O(N)
SC: O(1)
'''


def checkIfSorted(nums: list[int]) -> bool :

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True

def main():
    array = [1,2,3,4,5,4,6,2]
    answer = checkIfSorted(array)
    print(answer)
main()