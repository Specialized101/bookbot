import sys
from stats import count_words, count_characters, sort_stats

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(count_words(get_book_text(path)))
    print("--------- Character Count -------")
    stats = sort_stats(count_characters(get_book_text(path))) 
    for stat in stats:
        if stat["char"].isalpha():
            print(f"{stat['char']}: {stat['count']}")
    
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()