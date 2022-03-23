# Text Sorter

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
>>> i in text_sorter_data.items():
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

## What programming languages and tools have I used?

[<img align="left" alt="Python" width="26px" src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" style="padding-right:10px;" />](https://github.com/rodukov)
[<img align="left" alt="Debian" width="26px" src="https://www.debian.org/logos/openlogo-nd-100.png" style="padding-right:10px;" />](https://github.com/rodukov)
[<img align="left" alt="GitHub" width="26px" src="https://user-images.githubusercontent.com/3369400/139447912-e0f43f33-6d9f-45f8-be46-2df5bbc91289.png" style="padding-right:10px;" />](https://github.com/rodukov)
[<img align="left" alt="GitHub" width="26px" src="https://user-images.githubusercontent.com/3369400/139448065-39a229ba-4b06-434b-bc67-616e2ed80c8f.png" style="padding-right:10px;" />](https://github.com/rodukov)
