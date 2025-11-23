from stats import get_num_words
from stats import get_num_chars
from stats import sorted_list_dict

def get_book_text():
    with open("books/frankenstein.txt") as b:
        file_contents = b.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    words = get_num_words(get_book_text())
    print(f'Found {words} total words.')
    print("--------- Character Count -------")
    char_count = sorted_list_dict(get_num_chars)
    print(f'Found {dict_list} total characters.')

         

   

if __name__ == '__main__':
    main()
