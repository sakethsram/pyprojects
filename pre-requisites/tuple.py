# Tuple operations: counting occurrences, accessing index, concatenation, etc.

book_contents = (1, 2, 3, 4, 5, 2)
print(f"Book contents tuple: {book_contents}")

# counting occurrences of a specific item
page_2_count = book_contents.count(2)
print(f"Page 2 count: {page_2_count}")

# finding the index of a specific item
page_2_index = book_contents.index(2)
print(f"Index of first page 2: {page_2_index}")

# concatenating two tuples
extra_pages = (6, 7, 8)
all_pages = book_contents + extra_pages
print(f"All pages after concatenation: {all_pages}")

# slicing a tuple
first_three_pages = book_contents[:3]
print(f"First three pages: {first_three_pages}")

# using min() and max() to get the first and last pages
print(f"First page (min): {min(book_contents)}")
print(f"Last page (max): {max(book_contents)}")
s