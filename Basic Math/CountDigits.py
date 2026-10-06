'''
Question : Count digits in a number.

%10 to extract the rightmost digit
//10 to drop the rightmost digit

TC: O(LogN to base 10)
'''

def count_digits(num: int):

    count = 0

    while(num > 0):
        count += 1
        num = num // 10

    return count

def main():
    x = 11
    print(count_digits(x))
main()