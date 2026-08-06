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



