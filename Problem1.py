""" 
    Time Complexity: O(n^2)
    Space Complexity: O(n)

    Approach: 
    We create a dictionary and store the anagrams in it. 
    We use a prime product algorithm to find the prime factors of each string, since this gives us the key in a O(1) time complexity, unlike 
    sorting the strings, which takes O(nlogn) time.
    Then we iterate over the list of strings and check if the anagrams are already present in the dictionary. 
    If they are not present, we add them to the dictionary. 
    If they are present, we append the string to the list of strings. 
    Finally, we return the list of strings.
 """

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        def primeProduct(string):
            prime = [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                97,
                101,
                103,
            ]

            product = 1

            for ch in string:
                product *= prime[ord(ch) - ord("a")]

            return product

        for word in strs:
            pp = primeProduct(word)
            if pp in dic:
                dic[pp].append(word)
            else:
                dic[pp] = [word]
        res = []
        for key in dic:
            res.append(dic[key])

        return res
