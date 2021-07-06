sentence = input('Please enter a sentence:')

split_sentence = sentence.split(' ')
sorted_split = sorted(split_sentence)
split_sorted_set = set(sorted_split)

print(split_sorted_set)