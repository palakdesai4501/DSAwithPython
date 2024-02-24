#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
def isAnagram(self, s, t):
    str1_lo = s.lower()
    str2_lo = t.lower()

    return set(str1_lo) == set(str2_lo)

string1 = "hello"
string2 = "olleh"

result = isAnagram(string1, string2)

print(result)


