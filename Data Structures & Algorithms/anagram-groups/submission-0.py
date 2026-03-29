class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = set()
        anagram_list = []
        for i in range(0, len(strs)):
            while i not in visited:
                this_list = [strs[i]]
                anagram_map = {}
                for char in strs[i]:
                    if char in anagram_map:
                        anagram_map[char] += 1
                    else:
                        anagram_map[char] = 1
                
                for j in range(i+1, len(strs)):
                    if j not in visited and len(strs[i]) == len(strs[j]):
                        current_map = {}
                        for char in strs[j]:
                            if char in current_map:
                                current_map[char] += 1
                            else:
                                current_map[char] = 1

                        if current_map == anagram_map:
                            this_list.append(strs[j])
                            visited.add(j)
                        
                visited.add(i)
                anagram_list.append(this_list)
        return anagram_list
                                


            
        