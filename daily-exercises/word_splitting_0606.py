sentence = input('Please enter a sentence:')

split_sentence = sentence.split(' ')

split_set = set(split_sentence)
ordered = sorted(split_set, key=str.lower)

print(ordered)