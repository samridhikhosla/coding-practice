'''
Question: Give indexes of elements whose sum == target
TC: O(NLogN)
SC: O(N)
'''


def twoSum(nums: list[int], target: int) -> int :
    dict_position = {}

    for i in range(len(nums)):

        remaining = target - nums[i]

        if remaining not in dict_position.keys():
            dict_position[nums[i]] = i
        else:
            return[dict_position[remaining], i]

    return [-1, -1]

def main():
    array = [1, 2, 4, 7, 7, 5]
    k = 6
    answer = twoSum(array, k)
    print(answer)
main()
