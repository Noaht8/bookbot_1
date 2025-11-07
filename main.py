import sys
from stats import get_book_text, word_count, string_count, sort_dict
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    st = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(word_count(st))
    print("--------- Character Count -------")
    d = string_count(st)
    s_dict = sort_dict(d)
    for k, v in s_dict.items():
        print(f"{k}: {v}")
    print("============= END ===============")


main()
