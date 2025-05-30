class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = {}
        t_dict = {}
        if len(s) == len(t): #'aa' is not an anagram of 'a'
            for i in range(len(s)):
                if (s[i] not in s_dict):
                    s_dict[s[i]] = 1
                else:
                    s_dict[s[i]] += 1

            for j in range(len(t)):
                if (t[j] not in t_dict):
                    t_dict[t[j]] = 1
                else:
                    t_dict[t[j]] += 1

            for k in s_dict:
                if(k not in t_dict) or (s_dict[k] != t_dict[k]): #'abb' is not an anagram of 'aab'
                    return False
            return True
                
        else:
            return False
        
