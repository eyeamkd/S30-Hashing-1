"""
Time Complexity: O(n)
Space Complexity: O(n) ( if we are considering multi-linguistic characters O(1) constant if we are considering only lowercase english characters) 

Approach: 
We create separate dictionaries for both the strings and check if the characters are present in both dictionaries. 
If the characters are not present in both dictionaries, then they are not isomorphic. 
If the characters are present in both dictionaries, then we check if the characters are mapped to each other. 
If the characters are mapped to each other, then they are isomorphic. 
For a given character, we check if it is already mapped then if the mapping is correct else we map it to the other string.

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        dic_s = {}
        dic_t = {}

        for s_char, t_char in zip(s, t):
            if (s_char in dic_s and dic_s[s_char] != t_char) or (
                t_char in dic_t and dic_t[t_char] != s_char
            ):
                return False
            else:
                dic_s[s_char] = t_char
                dic_t[t_char] = s_char

        return True
