def get_word_count(book_content):
	book_split=book_content.split()
	word_count=len(book_split)
	return word_count

def get_letter_count(book_content):
	char_count={}
	book_content_lowercase=book_content.lower()
	for i in book_content_lowercase:
		if i not in char_count:
			char_count[i]=1
		else:
			char_count[i]+=1
	return char_count

def sort_char_count(char_count):
	def sort_on(chars):
		return chars["num"]
	list_to_sort=[]
	for i in char_count:
		list_to_sort.append({"char": i, "num": char_count[i]})
	list_to_sort.sort(reverse=True, key=sort_on)
	return list_to_sort
