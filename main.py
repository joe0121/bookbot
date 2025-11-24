from stats import get_num_words, get_num_chars, chars_dict_to_sorted_list

def get_book_text():
    with open("books/frankenstein.txt") as b:
        file_contents = b.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    text = get_book_text()
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
