# this is the performant solution using a sliding window technique
class solution_c:
    # input string returns int value of longest substring with
    # non-repeating values
    # this is the high speed solution
    def lengthOfLongestSubstring(self, input: str) -> int:
        # first figure out how long the string is
        length = len(input)
        # assume max length is 0
        max_length = 0
        # have a set, if the char appears in the set, it is repeating
        # the order actually doesn't matter for this solution
        # so set is fine
        # remember set only allows UNIQUE values
        char_set = set()
        # left pointer starts at 0 and right will start at the beginning as well
        left = 0


        # first iteration right is 0
        for right in range(length):
            # if the char at spot 0 has not yet been seen
            if input[right] not in char_set:
                # add to the set
                char_set.add(input[right])
                # basically take what is larger
                # either the CURRENT max_length
                # OR take the current pointer subract the left and
                # add 1 to make up for 0 based indexing
                max_length = max(max_length, right - left + 1)
            else:
                # otherwise we need to remove the non unique char
                while input[right] in char_set:

                    char_set.remove(input[left])
                    # advance the left pointer once per non-unique
                    # char
                    left = left + 1
                # finally re-add the char so it can now be unique
                # this handles the case of repeating chars occurring
                # earlier in the string
                char_set.add(input[right])
        # finally return the max length
        return max_length
