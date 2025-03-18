def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def count_words(text):
  words = text.split()
  return len(words)

def main():
  book_text = get_book_text("/home/jake/bookbot/books/frankenstein.txt")
  words_count = count_words(book_text)
  print(f"{words_count} words found in the document")

if __name__ == "__main__":
  main()