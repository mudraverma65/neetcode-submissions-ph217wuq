class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1, dict2 = {}, {}

        for s1 in s:
            if s1 in dict1:
                dict1[s1] += 1
            else:
                dict1[s1] = 1
        
        for s2 in t:
            if s2 in dict2:
                dict2[s2] += 1
            else:
                dict2[s2] = 1

        return dict1 == dict2
        