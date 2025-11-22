from stats import get_num_words
from stats import get_num_chars

def get_book_text():
    with open("books/frankenstein.txt") as b:
        file_contents = b.read()
    return file_contents

def main():
    words = get_num_words(get_book_text())
    print(f'Found {words} total words.')
    char_dict = get_num_chars(get_book_text())
    print(char_dict)
   

if __name__ == '__main__':
    main()
