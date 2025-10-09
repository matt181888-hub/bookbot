from stats import word_count
from stats import characters
from stats import sorted_character_dict
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    args = sys.argv
    try:
        books_path = args[1]
        text = get_book_text(books_path)
        lower_case_words = word_count(text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book at {books_path}...")
        print("----------- Word Count ----------")
        print(f" Found {len(lower_case_words)} total words")
        print("--------- Character Count -------")
        ind_characters = characters(lower_case_words)
        new_list = sorted_character_dict(ind_characters)
        print(new_list)
        print("============= END ===============")
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    

main()






    
    
        



