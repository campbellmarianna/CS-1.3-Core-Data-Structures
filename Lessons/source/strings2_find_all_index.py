def find_all_index(text, pattern):
    pattern_index = 0
    match = []
    # if pattern is empty, then return all indices
    if pattern == '':
        for index in range(len(text)):
            match.append(index)
        return match
    for index, charc in enumerate(text):
        # check if letters are the same
        if charc == pattern[pattern_index]:
            pattern_index += 1
            # if we've reached the end of the pattern index return the start of
            # the pattern in the text
            if pattern_index == len(pattern):
                match.append(index - (pattern_index - 1))
                pattern_index = 0
        # they are not the same
        else:
            pattern_index = 0
    if not match: # list is empty
        return None
    return match


if __name__ == '__main__':
    print(find_index('ababc', 'abc'))
