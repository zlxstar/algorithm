class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        last_S = ''
        for i in range(length):
            if S[i] == ' ':
                last_S = last_S + '%20'
            else:
                last_S = last_S + S[i]
        
        return last_S