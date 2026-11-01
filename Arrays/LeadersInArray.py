'''
Question: Return leaders in array ie everything on the right side of the element should be smaller
TC: O(N)
SC: O(N)
'''

def leadersInArr(nums: list[int]) -> list[int] : 

    ans_arr = []

    current = -100000000
    for i in range(len(nums) - 1, -1, -1): 
        if nums[i] > current:
            ans_arr.append(nums[i])
            current = nums[i]

    return ans_arr


def main():

    array = [10, 22, 12, 3, 0, 6]
    print(leadersInArr(array))

main()
