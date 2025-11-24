def get_num_words(text):
    words = text.split()
    return len(words)

#get the number of occurences of characters in a text inlcuding symbols and spaces


def get_num_chars(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(item):
    return item['num']

def chars_dict_to_sorted_list(char_dict): 
    
    dict_list = []
    
    for char, count in char_dict.items():
        small_dict = {"char": char, "num": count}
        dict_list.append(small_dict)
    
    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list    





