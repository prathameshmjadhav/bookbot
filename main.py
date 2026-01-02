from stats import count_words, count_characters, sorted_dictionary, set_file_path
import sys


def main():
    # print(get_book_text("./books/frankenstein.txt"))
    path_to_book = None
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"Found {count_words()} total words")    
    # print(count_characters())
    result = (sorted_dictionary())
    
    print(f"============ BOOKBOT ============ \n Analyzing book found at {sys.argv[1]}..\n----------- Word Count ----------\nFound {count_words()} total words \n--------- Character Count ------- \n")

    for item in result:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
        
    print("============= END ===============")

    
main()
