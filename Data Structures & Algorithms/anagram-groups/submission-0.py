class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # so we have a group of strings and we need to check whcih values are anagrams ie meaning they contain the same number of values and they are the same values. A rudimentary approach sees this as we take each string we turn it into a hash set and then do the same with each str and then compare against each hash and then group the sets and return the array. This would be roughly O(n^2). SO tldr for most optimal solution we set up a list dictionary, we then iterate through the strings with a array count of 26 0's from there we iterate through the characters in the string. from there we get the number of each character instance into the array and from there we use the count as an key made as a tuple and add the string to the list. and then we simply return the hash set. 

        anagrams = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 # this is to make an array with 26 characters
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            anagrams[tuple(count)].append(s)

        return list(anagrams.values())
        