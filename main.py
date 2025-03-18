from stats import count_words, count_characters

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  book_text = get_book_text("/home/jake/bookbot/books/frankenstein.txt")

  words_count = count_words(book_text)
  print(f"{words_count} words found in the document")

  char_count = count_characters(book_text)
  print(char_count)

if __name__ == "__main__":
  main()