""" 
Time Complexity: O(n)
Space Complexity: O(n)

Approach: 
We create two dictionaries for both the strings and check if the characters are present in both dictionaries. 
If the characters are not present in both dictionaries, then they are not following the same pattern. 
If the characters are present in both dictionaries, then we check if the characters are mapped to each other. 
If the characters are mapped to each other, then they are following the same pattern. 
For a given character, we check if it is already mapped then if the mapping is correct else we map it to the other string.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        dic1 = {}
        dic2 = {}
        s = s.split()

        if len(s)!= len(pattern):
            return False

        for char, word in zip(pattern, s):
            if (char in dic1 and dic1[char] != word) or (
                word in dic2 and dic2[word] != char
            ):

                return False
            else:
                dic1[char] = word
                dic2[word] = char

        return True
