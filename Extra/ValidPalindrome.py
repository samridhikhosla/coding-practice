class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        split_words = s.split()
        a_string = ""

        for i in range(len(split_words)):
            for j in split_words[i]:

                if (j.isalnum()): #i used isalpha() but somehow the website is failing it so..
                    a_string += j.lower()

        last_pointer = len(a_string) - 1
        
        for i in range(0, len(a_string)//2):
            if(a_string[i] != a_string[last_pointer]):
                return False

            else:
                if last_pointer > len(a_string) // 2:
                    last_pointer -= 1

        return True