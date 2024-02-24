#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
def isAnagram(self, s, t):
    str1_lo = s.lower()
    str2_lo = t.lower()
    
    #Checking the length of both string
    return set(str1_lo) == set(str2_lo)

string1 = "hello"
string2 = "olleh"

result = isAnagram(string1, string2)

print(result)


