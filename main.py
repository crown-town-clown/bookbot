def main():
	from stats import num_words, num_chars, sort_chars
	#print(num_chars())
	#print(sort_chars())

	print("============ BOOKBOT ============")
	print("Analyzying book found at books/frankenstein.txt...")
	print("------------ Word Count ---------")
	print(f"Found {num_words()} total words")
	print("----------- Character Count -----")
	chars = sort_chars()
	for char in chars:
		if char["char"].isalpha():
			print(f"{char["char"]}: {char["num"]}")
	print("============= END ===============")



main()
