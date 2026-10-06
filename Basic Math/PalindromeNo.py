'''
Question : Is the number a palindrome

TC: O(Log N to base 10)
'''

def palindrome_num(num: int):

    preserving_num = num
    reverse = 0

    while(num > 0):

        lastDigit = num % 10
        reverse = reverse * 10 + lastDigit
        num = num // 10

    if reverse == preserving_num:
        return True
    return False

def main():
    x = 14041
    print(palindrome_num(x))
main()