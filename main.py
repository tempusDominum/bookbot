def main():
    book_path = "books.frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    print(character_count)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_count = {}
    lowered_text = text.lower()
    for character in lowered_text:
        character_count[character] = character_count.get(character, 0) + 1 
    return character_count

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        # opens frankenstein text
        return f.read()

main()
