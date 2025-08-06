word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# list comprehension to create a new list with odd length of characters
odd_length_words = [word for word in word_list if len(word) % 2 != 0]
print("Words with odd length:", odd_length_words)
