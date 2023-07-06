# this solution works for the test cases but gets hung up on a case like
# "dvdf" because it has forgotten about the previous strings it has seen
# to get this to work it probably needs to go back a bit and rescan working on a full solution

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class SolutionToMostCases:
    # input string returns int value of longest substring with
    # non-repeating values
    def lengthOfLongestSubstring(self, input: str) -> int:
        # keep track of what has been seen
        # we don't care about knowing the value so use the size as key
        seen_chars = dict()
        # convert string into an array of chars
        input_as_ra = [*input]
        # temp_ra to keep track of what has been seen
        temp_ra = []
        # loop at speed O(n)
        for char in input_as_ra:
            if char not in temp_ra:
                temp_ra.append(char)
                # debug statement
                # print(temp_ra)
                seen_chars[len(temp_ra)] = temp_ra
                # debug statement
                # print(seen_chars)
            else:
                temp_ra = []
                temp_ra.append(char)
        # use built in max function at speed of O(n)
        # total setup should be O(2n) or O(n) linear time
        return max(seen_chars.keys(), default=0)
