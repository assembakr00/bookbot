def count_words(book_text):
    return len(book_text.split())

def get_chars_dict(text):
    chars_count = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in chars_count:
            chars_count[lowered_char] += 1
        else:
            chars_count[lowered_char] = 1
    return chars_count

def sort_on(char_sort: tuple[str, int]) -> int:
    return char_sort

def chars_dict_to_sorted_list(chars_count: dict[str, int]) -> list[tuple[str, int]]:

    sort_list = []

    for char in chars_count:
        count = chars_count[char]
        sort_list.append((char, chars_count[char]))
    
    sorted_list = sorted(sort_list, key=sort_on, reverse=True)

    return sorted_list

