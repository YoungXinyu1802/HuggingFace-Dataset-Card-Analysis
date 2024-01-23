---
license: openrail
---

Dataset Summary
---
Collection of Romance Novels featuring `title`, `description`, and `genres`. Created with intention of building a "Romance Novel Generator."

Data Fields
---
- `id` : unique integer to id book in the dataset
- `pub_month` : string indicating the month the book was published in the form: `YEAR_MONTH`
- `title` : title of the book
- `author` : comma-separated (`last-name, first-name`) of the author of book 
- `isbn13` : 13 digit number for the isbn of book (note not all books will have an isbn number)
- `description` : text description of the book. May contain quoted lines, a brief teaser of the plot, etc...
- `genres` : dictionary of all genres with 0 indicating the book is **NOT** tagged to that genre, and a 1 indicating that the book is tagged to that genre
 - additional fields are the all the individual genres exploded with respective 1 & 0 values

Languages
--
- en