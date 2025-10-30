import sys
from stats import (
    book_text_words,
    character_count,
    dict_to_sorted_list,
)

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(sys.argv[1])
    num_words = book_text_words(book_text)
    char_dict = character_count(book_text)
    chars_sorted_list = dict_to_sorted_list(char_dict)
    final_print(book_path, num_words, chars_sorted_list)

def final_print(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()