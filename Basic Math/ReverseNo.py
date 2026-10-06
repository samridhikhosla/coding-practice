'''
Question : Reverse a number

TC: O(Log N to base 10)
'''

def reverse_digits(num: int):

    reverse = 0

    while(num > 0):
        lastDigit = num % 10
        reverse = reverse * 10 + lastDigit
        num = num // 10

    return reverse

def main():
    x = 14056
    print(reverse_digits(x))
main()