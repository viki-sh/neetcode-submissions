class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        
        s = list(s)
        t = list(t)

        if len(s) != len(t): 
            return False

        for i in range(len(s)):
            if s[i] not in s_dict: 
                s_dict[s[i]] = 1
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            if s[i] in s_dict: 
                s_dict[s[i]] += 1
            if t[i] in t_dict: 
                t_dict[t[i]] += 1
        
        return s_dict == t_dict
            