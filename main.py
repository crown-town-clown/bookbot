def main():
	import sys
	from stats import num_words, num_chars, sort_chars
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		path_to_book = sys.argv[1]
		print("============ BOOKBOT ============")
		print(f"Analyzying book found at {path_to_book}...")
		print("------------ Word Count ---------")
		print(f"Found {num_words(path_to_book)} total words")
		print("----------- Character Count -----")
		chars = sort_chars(path_to_book)
		for char in chars:
			if char["char"].isalpha():
				print(f"{char["char"]}: {char["num"]}")
		print("============= END ===============")



main()
