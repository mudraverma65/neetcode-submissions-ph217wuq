class Solution:
    def __init__(self):
        self.index = []

    def encode(self, strs: List[str]) -> str:
        self.index = []
        encrypted = ''
        for current_str in strs:
            self.index.append(len(current_str))
            encrypted += current_str
        return encrypted


    def decode(self, s: str) -> List[str]:
        decrypted = []
        prev_index = 0
        for i in self.index:
            decrypted.append(s[prev_index:prev_index+i])
            prev_index += i
            
        return decrypted

