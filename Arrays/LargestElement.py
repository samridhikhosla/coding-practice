'''
Question: Largest elements in array
TC: O(N)
SC: O(1)
'''

def largestElement(nums: list[int]) -> int :

    max = -1
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]

    return max

def main():
    array = [3,2,1,5,2]
    answer = largestElement(array)
    print(answer)
main()