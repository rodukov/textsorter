# textsorter

This simple script sorts all the words in the text by popularity in descending order.

## How to install it?

```bash
git clone https://github.com/rodukov/textsorter
cd textsorter
```

## How to use it?

You can use this script in your projects. You only need to import it:

```python
>>> from textsorter import textsorter
>>> your_text = "Hello, Hello how are you?"
>>> sorted_text = textsorter.sort_text(your_text)
>>> print(sorted_text)
{'Hello': 2, 'how': 1, 'are': 1, 'you': 1}
```

## How do you make the data output look nice?

We will use the beautiful tables module:

```bash
pip3 install beautifultable
```

```python
>>> from beautifultable import BeautifulTable
>>> table = BeautifulTable()
>>> text_sorter_data = {'Hello': 2, 'how': 1, 'are': 1, 'you': 1}
>>> for i in text_sorter_data.items():
...	table.rows.append([i[0], i[1]])
...
>>> table.columns.header = ["Word", "Count"]
>>> print(table)
+-------+-------+
| Word  | Count |
+-------+-------+
| Hello |   2   |
+-------+-------+
|  how  |   1   |
+-------+-------+
|  are  |   1   |
+-------+-------+
|  you  |   1   |
+-------+-------+
```
