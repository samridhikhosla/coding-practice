'''
Question: Rearrange array elements by sign in order, pos and negs are same in number
TC: O(N)
SC: O(N)
'''

def rearrangeBySign(nums: list[int]) -> list[int] : #O(2N) TC, O(N) SC

    pos_arr = []
    negs_arr = []

    for i in range(len(nums)):
        if nums[i] >= 0 :
            pos_arr.append(nums[i])
        else:
            negs_arr.append(nums[i])

    ans_arr = [0,0,0,0,0,0]

    for i in range(len(pos_arr)):
            ans_arr[i * 2] = pos_arr[i]
            ans_arr[i * 2 + 1] = negs_arr[i]

    return ans_arr


def rearrangeBySignBetter(nums: list[int]) -> list[int] :

    ans_arr = [0,0,0,0,0,0]
    pos_index = 0
    neg_index = 1

    for i in range(len(nums)):
        if nums[i] < 0:
            ans_arr[neg_index] = nums[i]
            neg_index += 2
        else:
            ans_arr[pos_index] = nums[i]
            pos_index += 2

    return ans_arr

def main():

    array = [3, 1, -2, -5, 2, -4]
    print(rearrangeBySign(array))
    print(rearrangeBySignBetter(array))

main()
