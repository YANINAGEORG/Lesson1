def single_root_words(root_word, *other_words):
    same_words = []

    for i in other_words:
        if root_word.lower() in i:
            same_words.append(i)
        if i.lower() in root_word.lower():
            same_words.append(i)
    print(*same_words)

single_root_words('Anna', 'Vanna', 'an', 'Bob', 'Bananna')