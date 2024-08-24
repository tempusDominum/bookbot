def main():
    book_path = "books.frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_list = count_characters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for character, count in character_list:
        print(f"The '{character}' character was found {count} times")
    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_count = {}
    lowered_text = text.lower()
    for character in lowered_text:
        if character.isalpha():
            character_count[character] = character_count.get(character, 0) + 1
    character_list = list(character_count.items())
    character_list.sort(reverse=True, key=lambda character_count: character_count[1])
    return character_list

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        # opens frankenstein text
        return f.read()

main()
