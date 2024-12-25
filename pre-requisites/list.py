# List operations: append, extend, remove, sort, slice, etc.

book_pages = [1, 2, 3, 4, 5]
print(f"Initial pages: {book_pages}")

# appending a new page
book_pages.append(6)
print(f"After appending new page: {book_pages}")

# extending with additional pages
book_pages.extend([7, 8])
print(f"After extending with new pages: {book_pages}")

# inserting a page at a specific position
book_pages.insert(3, 99)
print(f"After inserting a special page: {book_pages}")

# removing a page by value
book_pages.remove(99)
print(f"After removing the special page: {book_pages}")

# sorting the pages in descending order
book_pages.sort(reverse=True)
print(f"Sorted pages in descending order: {book_pages}")

# slicing the pages
sliced_pages = book_pages[1:4]
print(f"Sliced pages: {sliced_pages}")

# list comprehension to get even pages
even_pages = [page for page in book_pages if page % 2 == 0]
print(f"Even pages using list comprehension: {even_pages}")

# clearing the list (like removing all pages from a book)
book_pages.clear()
print(f"After clearing the pages: {book_pages}")
