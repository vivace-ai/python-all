sentence = input("문장: ")

words = sentence.split()
print(f"단어 수: {len(words)}")
print(f"가장 긴 단어: {max(words, key=len)}")
