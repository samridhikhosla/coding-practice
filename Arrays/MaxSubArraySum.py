'''
Question : Find the maximum sub array sum.

Kadane's algorithm : an efficient method to solve the maximum subarray problem 
by finding a contiguous subarray with the largest sum in a one-dimensional array.

TC: O(N)
SC: O(1)
'''

def maxSum(nums: list[int]):

    sum = 0
    maxi = -100000

    for i in range(len(nums)):

        sum += nums[i]

        if maxi < sum:
            maxi = sum

        if sum < 0:
            sum = 0

    return maxi
   

def main():
    x = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maxSum(x))
main()