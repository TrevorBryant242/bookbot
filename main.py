import sys

from stats import get_num_words
from stats import get_num_chars
from stats import get_book_text
#from stats import sort_dict

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>") 
	sys.exit(1)
else: 
	book_path = sys.argv[1]

def main():
	global book_path
	
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	num_char = get_num_chars(text)
	
	
	
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	sort_dict(num_char)
	print("============= END ===============")



def sort_dict(num_char):
    sorted_dict = dict(sorted(num_char.items(), key=lambda item: item[1], reverse=True))
    for i in sorted_dict:
	    if i.isalpha():
		    print(f"{i}: {sorted_dict[i]}")




main()

