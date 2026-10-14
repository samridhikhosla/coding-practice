'''
Question: Find the majority element (appearing more than n/2 times)
Moore's Voing algorithm
TC: O(2N)
SC: O(1)
'''

def findMajority(nums: list[int]) -> int :

    count = 0
    element = -1

    for i in range(len(nums)):

        if count == 0:
            element = nums[i]
            count = 1

        elif nums[i] == element:
            count += 1

        else:
            count -= 1

    return checkMajority(nums, element)

def checkMajority(nums, element: int): #in this question, it is not guarenteed if there is a majority fs

    count = 0
    for i in range(len(nums)):
        if element == nums[i]:
            count += 1

    if count >= len(nums)//2:
        return element
    else:
        return 'no clear majority byeeeee'
    
def main():

    array = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5]
    answer = findMajority(array)
    print(answer)

main()

'''
If hashmap used to count the freq.
TC: O(2N)
SC: O(N)
'''