# 3. Longest Substring Without Repeating Characters - Medium

# Given a string s, find the length of the longest substring without repeating characters.

# O(n), where n is the length of the input string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        unique = set()
        max_length = 0
        
        while j < len(s):
            if s[j] not in unique:
                unique.add(s[j])
                max_length = max(max_length, j - i + 1)
                j += 1
            else:
                unique.remove(s[i])
                i += 1
                
        return max_length
