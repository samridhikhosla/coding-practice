class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_list = [] #[['a','b'],['c','d']]
        for i in range(len(strs)):
            b_list = []
            for j in strs[i]:
                b_list.append(j)
            a_list.append(b_list)

        a_dict = {}
        
        for i in range(len(strs)):
            unique_key = ''.join(sorted(a_list[i]))
            if(unique_key not in a_dict):
                a_dict[unique_key] = [a_list[i]]
            
            else:
                a_dict[unique_key].append(a_list[i])

        result_list = []
        for values in a_dict.values():

            mini_list = []
            for i in values:
                joined_strs = ''.join(i)
                mini_list.append(joined_strs)
            
            result_list.append(mini_list)
                
        return result_list