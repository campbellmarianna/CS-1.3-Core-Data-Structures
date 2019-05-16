#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    result = find_index(text, pattern)
    # if the pattern is not found in
    if result is None:
        return False
    if result >= 0:
        # return result
        return True

    # if pattern == '':
    #     return 0
    # for t_index, t_char in enumerate(text): # 0(t)
    #     for p_index, p_char in enumerate(pattern): # 0(p)
    #         # check if more characters in the text match characters in the pattern
    #         text_char = text[t_index + p_index]
    #         # check if letters are the same
    #         if text_char == p_char:
    #             continue
    #         # they are not the same
    #         else:
    #             break
    #     else:                                                                     # Really helpful resource to find solution: https://www.python-course.eu/python3_for_loop.php
    #         # all characters in the pattern matched in the text
    #         return True
    #
    # # tried all possible starting indexes in text, never found a perfect match
    # return False


def find_index(text, pattern, start_index=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if pattern == '':
        return 0
    # Before we check the text and pattern lets make sure the pattern occurs in the text
    for t_index, t_char in enumerate(text):
        for p_index, p_char in enumerate(pattern):
            # check if more characters in the text match characters in the pattern
            text_char = text[t_index + p_index]
            # check if letters are the same
            if text_char == p_char:
                continue
            # they are not the same
            else:
                break
        else:                                                                     # Really helpful resource to find solution: https://www.python-course.eu/python3_for_loop.php
            # all characters in the pattern matched in the text
            return t_index

    # tried all possible starting indexes in text, never found a perfect match
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # def find_all_index(text, pattern):
    match = []
    if pattern == '':
        for index in range(len(text)):
            match.append(index)
        return match
    for t_index, t_char in enumerate(text):
        for p_index, p_char in enumerate(pattern):
            # check if more characters in the text match characters in the
            # pattern
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
    # all characters in the pattern matched in the text
    return match

# if this pattern is contained in the text
# get this functions find_index property and return that
# get this functions find_all_index property and return that


def test_string_algorithms(text, pattern):
    # found = contains(text, pattern)
    # print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # # TODO: Uncomment these lines after you implement find_index
    # index = find_index(text, pattern)
    # print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()
    # print(find_all_indexes('aaaaa', 'aa'))
    print(contains('abcabc', 'abcb'))
