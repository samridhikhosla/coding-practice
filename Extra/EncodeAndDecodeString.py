class Solution:
    '''
    lets say if a word is he#llo
    then the length will determine till where we have to keep reading
    so encoding in len + # + word
    '''

    def encode(self, strs: list[str]) -> str:

        encode_string = ""

        for i in range(len(strs)):
            encode_string += str(len(strs[i])) + "#" + strs[i]

        return encode_string

    def decode(self, s: str) -> list[str]:
        
        decode_list = []
        i = 0

        while i < len(s):
            j = i
            length_of_word = ""

            while s[j] != "#" and s[j].isdigit():
                length_of_word += s[j]
                j += 1

            length_of_word = int(length_of_word)
            i = j + int(length_of_word) + 1
            decode_list.append(s[j + 1: length_of_word + j + 1])

        return decode_list