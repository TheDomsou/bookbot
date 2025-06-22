import sys

from stats import get_word_count

from stats import get_letter_count

from stats import sort_char_count

def get_book_text(filepath):
    with open(filepath) as f:
         file_contents=f.read()
    return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	filepath=sys.argv[1]
	book_content=get_book_text(filepath)
	word_count=get_word_count(book_content)
	letter_count=get_letter_count(book_content)
	sorted_list=sort_char_count(letter_count)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for i in sorted_list:
		if i["char"].isalpha():
			print(f"{i['char']}: {i['num']}")
	print("============= END ===============")

main()
