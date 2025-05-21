def get_book_text(path_to_book):
	with open(path_to_book) as f:
		file_contents = f.read()
	return file_contents

def num_words(path_to_book):
	words = get_book_text(path_to_book).split()
	return len(words) 

def num_chars(path_to_book):
	chars = {}
	book_text = get_book_text(path_to_book).lower()
	for char in book_text:
		if char not in chars:
			chars[char] = 1			
		else:
			chars[char] += 1
	return chars

def sort_on(dict):
	return dict["num"]

def sort_chars(path_to_book):
	chars = num_chars(path_to_book)
	list_of_chars = []
	for char in chars:
		char_dict = {}
		char_dict["char"] = char
		char_dict["num"] = chars[char]
		list_of_chars.append(char_dict)
	list_of_chars.sort(reverse=True, key=sort_on)
	return list_of_chars

