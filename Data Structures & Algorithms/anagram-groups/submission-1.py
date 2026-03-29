class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []

        seen_chars = {}

        for i in range(len(strs)):
            char_frequency = 26 * [0]
            for c in strs[i]:
                index = ord(c) - ord('a')
                char_frequency[index] += 1
            char_frequency = tuple(char_frequency)    
            if char_frequency in seen_chars:
                anagrams[seen_chars[char_frequency]].append(strs[i])
            else:
                seen_chars[char_frequency] = len(anagrams)
                anagrams.append([strs[i]])

        return anagrams
        