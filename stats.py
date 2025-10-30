def book_text_words(book_text):
    words = book_text.split()
    return len(words)

def character_count(book_text):
    char_dict = {}
    lowercase_book_text = book_text.lower()
    lowercase_words_list = lowercase_book_text.split()

    for word in lowercase_words_list:
        for i in range(0,len(word)):
            if word[i] in char_dict:
                char_dict[word[i]] += 1
            else:
                char_dict[word[i]] = 1

    return char_dict

def sorter(d):
    return d["num"]

def dict_to_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=sorter)
    return sorted_list