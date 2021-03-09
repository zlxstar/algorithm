class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        last_s = ''
        for i in range(len(indices)):
            last_s = last_s + s[indices.index(i)];
        
        return last_s