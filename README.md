yes24-py
========
yes24.com api


installation
------------
```pip install yes24```


require
-------
beautifulsoup4, lxml


usage
-----
```
from yes24 import Yes24
book = Yes24(6694057)
print book.title, book.author, ...
```

book infos
----------
title, author, price, date, pages, weight, size, url