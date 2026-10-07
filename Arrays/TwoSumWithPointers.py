'''
Question: Give indexes of elements whose sum == target without HASHING
TC: O(N + NLogN)
SC: O(N)
'''


def twoSum(nums: list[int], target: int) -> int :

    nums.sort()

    left = 0
    right = len(nums) - 1

    while(left < right):

        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left = left + 1
        else:
            right = right - 1

    return [-1, -1]

def main():
    array = [1, 2, 4, 7, 7, 5]
    k = 6
    answer = twoSum(array, k)
    print(answer)
main()
