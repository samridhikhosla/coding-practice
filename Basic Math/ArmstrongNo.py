'''
Question : True if it is an armstrong number
Armastrong number is eg. 371 = 3^3 + 7^3 + 1^3 = 371
TC: O(Log N base to N)
SC: O(1)
'''

def isArmstrong(num: int):

    sum = 0
    temp = num

    while(num> 0):
        lastDigit = num % 10
        sum = sum + (lastDigit * lastDigit * lastDigit)
        num = num // 10

    if sum == temp:
        return True
    return False

def main():
    x = 371
    print(isArmstrong(x))
main()