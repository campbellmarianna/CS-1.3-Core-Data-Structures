# Input: "abac", "ba" # text and pattern
# print("t_char: {}, t_index: {}, Pattern {}, Pattern Index: {},".format(t_char, t_index, pattern[pattern_index], pattern_index))
def find_index(text, pattern):
    print("Pattern length", len(pattern))
    # pattern_index = 0
    # All strings contains empty string
    if pattern == '':
        return t_index
    for t_index, t_char in enumerate(text):
        print("Text Character {}".format(t_char))
        # check if letters are the same
        for p_index, p_char in enumerate(pattern):
            print("Pattern Character {}".format(p_char))
            text_char = text[t_index + p_index]
            if text_char == p_char:
                # pattern_index += 1
                continue
                # if we've reached the end of the pattern index return
                # the start of
                # the pattern in the text
                # if pattern_index == len(pattern):
                #     return t_index - (pattern_index - 1)
            # they are not the same
            else:
                # pattern_index = 0
                break
        else:                                                                     # Really helpful resource to find solution: https://www.python-course.eu/python3_for_loop.php
            # all characters in the pattern matched in the text
            return t_index

    # tried all possible starting indexes in text, never found a perfect match
    return None

if __name__ == '__main__':
    print(find_index('abby', 'by'))
