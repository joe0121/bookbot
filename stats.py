def get_num_words(text):
    words = text.split()
    return len(words)

#get the number of occurences of characters in a text inlcuding symbols and spaces

char_dict = {}
char_count = 0

def get_num_chars(text):
    text = text.lower()
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sorted_list_dict(char_dict):
    
    char.dict.sort()