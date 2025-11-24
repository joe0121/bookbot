from stats import get_num_words, get_num_chars, chars_dict_to_sorted_list
import sys

def check_args(): 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  


def get_book_text(path_to_book):
    with open(path_to_book) as b:
        file_contents = b.read()
    return file_contents

def main():
    check_args()
    path_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    text = get_book_text(path_to_book)
    words = get_num_words(text)
    char_dict = get_num_chars(text)
    print(f'Found {words} total words')
    print("--------- Character Count -------")
    chars_sorted_list = chars_dict_to_sorted_list(char_dict)
    for item in chars_sorted_list:
        ch = item['char']
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")
    print("============= END ===============")

         

   

if __name__ == '__main__':
    main()
