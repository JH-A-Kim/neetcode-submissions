class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # so we have 2 strings and if they are anagrams meaning they are can spell each other out. What this is basically checking is if there is the same number of each value in a string. So my basic intuition is that we iterate through one string and take note of the number of each value and compare the numbers against each other. so for example in racecar and carrace i see r=1 i check carrace set and see r is also = to 1 therefore i move forward. and continuing on until i either find one that is not or one that is. 
        string1 = {}
        string2 = {}
        for letter in s:
            if letter not in string1:
                string1[letter]=1
            else:
                string1[letter]+=1
        
        for letter in t:
            if letter not in string2:
                string2[letter]=1
            else:
                string2[letter]+=1

        if string1 == string2:
            return True
        else:
            return False
        