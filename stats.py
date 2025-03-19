def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
  char_count = {}
  lowercase_text = text.lower()
  for char in lowercase_text:
    char_count[char] = char_count.get(char,0) + 1
  return char_count

def get_sorted_key(char_dict):
  return (-char_dict['count'], char_dict['character'])

def sort_character_counts(char_count):
  filtered_chars = {}
  char_list = []
  
  for char, count in char_count.items():
    if char.isalpha():
      filtered_chars[char] = count

  for char, count in filtered_chars.items():
    char_dict = {'character': char, 'count': count}
    char_list.append(char_dict)

  sorted_char_list = sorted(char_list, key=get_sorted_key)

  return sorted_char_list

  