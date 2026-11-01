'''
Question: Find a number that appears once and others twicein an array
TC: O(N)
SC: O(1)
'''

def findMissingXOR(nums: list[int]) -> int :

    xor = 0

    for i in range(len(nums)):
        xor ^= nums[i]
    return xor


def main():

    array = [1,1,2,2,4,5,5]
    print(findMissingXOR(array))

main()
