'''
Question : Count odd digits in a number.

TC: O(LogN to base 10)
'''

def count_odd_digits(num: int):

    count = 0
    while(num > 0):
        lastDigit = num % 10

        if lastDigit % 2 != 0:
            count += 1

        num = num // 10

    return count
   

def main():
    x = 12835
    print(count_odd_digits(x))
main()