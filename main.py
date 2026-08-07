import sys
from stats import count_words, get_chars_dict, chars_dict_to_sorted_list


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_content = get_book_text(book_path)
    num_words = count_words(book_content)
    character_frequencies = get_chars_dict(book_content)
    sorted_chars_list = chars_dict_to_sorted_list(character_frequencies)

    print_report(book_path, num_words, sorted_chars_list)


def print_report(book_path, word_count, sorted_chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char, count in sorted_chars_list:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

    print("============= END =============")


main()

