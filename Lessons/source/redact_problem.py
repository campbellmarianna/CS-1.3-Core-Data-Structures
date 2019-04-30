def redact_words(words, banned_words):
    new_words = []
    for word in words:
        for index, banned_word in enumerate(banned_words):
            if word != banned_word and index == len(banned_words) - 1:
                new_words.append(word)
            continue
    return new_words

if __name__ == '__main__':
    # redact_words()
    print(redact_words(['fluffy', 'bad', 'superbad', 'good'], ['bad', 'superbad']) )
