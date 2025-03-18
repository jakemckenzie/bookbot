def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
  char_count = {}
  lowercase_text = text.lower()
  for char in lowercase_text:
    char_count[char] = char_count.get(char,0) + 1
  return char_count