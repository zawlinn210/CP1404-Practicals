"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""
text = input("Text: ")
sorted_words = sorted(text.split(" "))
count_occurrences = {word: sorted_words.count(word) for word in sorted_words}
for word in count_occurrences:
    print(word, ":", count_occurrences[word])