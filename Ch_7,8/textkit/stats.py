
# Count words in text
def word_count(text):
    return len(text.split())


# Find the longest word
def longest_word(text):
    words = text.split()
    return max(words, key=len)
