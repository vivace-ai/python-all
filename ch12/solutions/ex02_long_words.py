sentence = "python makes data analysis simple and readable"

long_words = [word.upper() for word in sentence.split() if len(word) >= 6]
print(long_words)
