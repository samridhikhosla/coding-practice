class Solution:
    def groupAnagrams(self, strs: list[str]):

        a_list = [] #[['a','b'],['c','d']]
        for i in range(len(strs)):
            b_list = []
            for j in strs[i]:
                b_list.append(j)
            a_list.append(b_list)

        a_dict = {}
        
        for i in range(len(a_list)):
            a_dict[i] = sorted(a_list[i])

        for i in range(len(a_list)):
            print(sorted(a_list[i]))
            
            # sorted_list.append(sorted(a_list[i]))
            '''
            in progress
            '''
        

def main():
    sol = Solution()
    sol.groupAnagrams(["act","pots","tops","cat","stop","hat"])

main()