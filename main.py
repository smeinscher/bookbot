from stats import get_word_count, get_character_count, get_sorted_character_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    book_content = get_book_text(sys.argv[1])
    print(f"Found {get_word_count(book_content)} total words")
    print("--------- Character Count -------")
    character_counts = get_character_count(book_content)
    character_list = get_sorted_character_list(character_counts);
    for item in character_list:
        if (item["char"].isalpha()):
            print(f"{item["char"]}: {item["num"]}");
    print("============= END ===============");
main();
