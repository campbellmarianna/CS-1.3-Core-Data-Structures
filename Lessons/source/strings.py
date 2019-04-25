#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)
    # Keeping track of target values
    target_length = len(pattern) - 1
    target_index = 0
    # Keeping track of text values
    text_length = len(text) - 1
    text_index = 0

    match = None
    # All strings contains empty string
    if pattern == '':
        return True
    # Check if we passed the end of the text or the pattern
    while target_length >= target_index and text_length >= text_index:
        # Checking if current pattern and text letters match
        if pattern[target_index] == text[text_index]:
            target_index += 1
            text_index += 1
            # If we passed the end of the pattern only then we have found the match
            if target_index > target_length:
                return True
        # If it is not a match and were still on the first letter of the pattern
        # then increment text_index
        elif pattern[target_index] != text[text_index] and target_index == 0:
            text_index += 1
        # If it is not a match and were past the first letter of the pattern
        # reset the pattern index
        elif pattern[target_index] != text[text_index] and target_index > 0:
            target_index = 0

    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if pattern == '':
        return 0
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
    main()
    # print(find_all_indexes('aaaaa', 'aa'))
