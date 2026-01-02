import sys;

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]  
text_dictionary = {}

def set_file_path(arg_path):
    filepath = arg_path

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words():
    file_contents = get_book_text(filepath)
    arr = file_contents.split()
    return len(arr)

def count_characters():
    file_contents = get_book_text(filepath)
    arr = file_contents.split()

    for word in arr:
        for text in word:
            if text.lower() in text_dictionary:
                text_dictionary[text.lower()]+=1
            else:
                text_dictionary[text.lower()] = 1
    return text_dictionary

def sorted_dictionary():
    text_dictionary = count_characters()
    word_count = count_words()
    sorted_list = []

    # sort the dictionary
    # take each element from the text_dictionary add it to the list in the format {"char": "b", "num": 2}
    # Use a helper function to return the "num" of each dictionary for comparison
    # Sort the list from greater to least by num count

    for item in text_dictionary:
        sorted_list.append({"char": item, "num":text_dictionary[item]})

    def sort_on(items):
        return items["num"]

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

