def get_num_words(text):
	words = text.split()
	return len(words)
#gets number of words in the book


def get_num_chars(text):
	char_list = {}
	for char in text:
		lowered = char.lower()
		if lowered in char_list:
			char_list[lowered] += 1
		else:
			char_list[lowered] = 1
	return char_list
#gets number of each char in the book

def get_book_text(path):
    with open(path) as f:
        return f.read()
	
# reads text of book and sends to terminal as string




#sorts the dictionary of words