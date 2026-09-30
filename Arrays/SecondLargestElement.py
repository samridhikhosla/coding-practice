'''
Question: Second largest element in array
TC: O(N)
SC: O(1)
'''

def secondLargestElement(nums: list[int]) -> int :

    lastElement = nums[0]
    secondLast = -1

    for i in range(1, len(nums)):
        if nums[i] > lastElement:      
            secondLast = lastElement
            lastElement = nums[i]

        elif nums[i] < lastElement and nums[i] > secondLast:
            secondLast = nums[i]

    return secondLast

def main():
    array = [1, 2, 4, 7, 7, 5]
    answer = secondLargestElement(array)
    print(answer)
main()

'''
Brute force solution: sort the list, then pick up n-2th element if n-2th element != max/largest/n-1th
TC: O(NlogN + N)
'''