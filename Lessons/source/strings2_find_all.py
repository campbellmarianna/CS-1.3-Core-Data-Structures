# def find_all_index(text, pattern):
    # pattern_index = 0
    # match = []
    # # if pattern is empty, then return all indices
    # if pattern == '':
    #     for index in range(len(text)):
    #         match.append(index)
    #     return match
    # for index, charc in enumerate(text):
    #     # check if letters are the same
    #     if charc == pattern[pattern_index]:
    #         pattern_index += 1
    #         # if we've reached the end of the pattern index return the start of
    #         # the pattern in the text
    #         if pattern_index == len(pattern):
    #             match.append(index - (pattern_index - 1))
    #             pattern_index = 0
    #     # they are not the same
    #     else:
    #         pattern_index = 0
    # if not match: # list is empty
    #     return None
    # return match
def find_all_index(text, pattern):
    match = []
    if pattern == '':
        for index in range(len(text)):
            match.append(index)
        return match
    for t_index, t_char in enumerate(text):
        print("t_index: ", t_index)
        for p_index, p_char in enumerate(pattern):
            # check if more characters in the text match characters in the
            # pattern
            print("  p_index {}, p_char {}".format(p_index, p_char))
            # check if it is a valid index of the text
            if t_index + p_index > (len(text)-1):
                break # not a valid index
            text_char = text[t_index + p_index]
            # check if letters are the same
            if text_char == p_char:
                # check if the letters are the same and we've reached the last
                # index of the pattern
                if p_index == (len(pattern) - 1):
                # append the position of the charc where the pattern and text
                    # first matched
                    match.append(t_index)
                    # append the text index minus the pattern index
                continue
            # they are not the same
            else:
                break
    if not match: # check if match is empty                                                                    # Really helpful resource to find solution: https://www.python-course.eu/python3_for_loop.php
        # tried all possible starting indexes in text, never found a perfect match
        return None
    # all characters in the pattern matched in the text
    return match




if __name__ == '__main__':
    print(find_all_index('aaa', 'aa'))
