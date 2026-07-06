class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_Anagram = False
        for i in range(len(s)):
            if len(s) == len(t):
                if s[i] in t:
                    is_Anagram = True
                else:
                    is_Anagram = False
            else:
              is_Anagram = False
              break  
        
        return is_Anagram



            

        
