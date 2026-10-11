'''
Question : Reverse a number

TC: O(log n to base 10)
'''

def revNo(nums: int):

    rev = 0

    while(nums>0):
        lastDigit = nums % 10
        rev = rev * 10 + lastDigit
        nums = nums // 10

    return rev
   

def main():
    x = 2098
    print(revNo(x))
main()