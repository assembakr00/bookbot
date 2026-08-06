from stats import count_words, get_chars_dict, chars_dict_to_sorted_list


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path)
    num_words = count_words(book_content)
    character_frequencies = get_chars_dict(book_content)

    print(print_report)

def print_report():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path)
    num_words = count_words(book_content)
    for char in chars_dict_to_sorted_list(character_frequencies):
        str.isalpha

    print(f"Found {num_words} total words")
    print(chars_dict_to_sorted_list(character_frequencies))
    print(====================END=======================)

main()

