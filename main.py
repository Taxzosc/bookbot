from stats import count_num_words, lower_and_count_letters, sorted_dictionary
import sys

# gets a text file and that it reads and saves to a variable
def get_book_text(file):
    if len(file) != 2:
        raise  Exception("Usage: python3 main.py <path_to_book>")
    else:
        with open(file[1]) as f:
            file_contents = f.read()
            return file_contents


def main():
    path_to_file = sys.argv # ["python file", "path to book file"] makes a list over the input in the terminal
    try:
        book = get_book_text(path_to_file)
    except Exception as e:
        print(e)
        sys.exit(1)
    word_count = count_num_words(book) #counts the number of words in a text
    letter_count = lower_and_count_letters(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_dictionary(letter_count)
    print("============= END ===============")

main()