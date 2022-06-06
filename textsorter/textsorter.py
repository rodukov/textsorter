class textsorter:
	def sort_text(text: str, _blacklisted_symbols: list = ["!", "?", ".", ",", "(", ")"]) -> dict:
		"""This function will return all words from the text sorted by mentionability and descending"""
		text = text.split()
		# Remove unnecessary characters from the text
		for i, k in enumerate(text):
			for _symbol in _blacklisted_symbols:
				if _symbol in text[i]:
					text[i] = k.replace(_symbol, "")
		# Count the number of words in the text
		sorted_text = {}
		for i in text:
			if (i not in sorted_text): sorted_text[i] = 1
			else: sorted_text[i] += 1
		return { k: v for k, v in sorted(sorted_text.items(), key=lambda item: item[1], reverse=True) }
