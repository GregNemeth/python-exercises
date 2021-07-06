sentence = input('Please enter a sentence:')

def alphasort(sentence):

    split_sentence = sentence.split(' ')

    split_set = set(split_sentence)
    ordered = ' '.join(sorted(split_set, key=str.lower))
    return ordered

print(alphasort(sentence))