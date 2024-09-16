def single_root_words(root_word, *other_words):
    same_words = []

    for words in other_words:
        if root_word.lower() in words.lower():
            same_words.append(words)

        elif words.lower() in root_word.lower():
            same_words.append(words)

    print(same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')