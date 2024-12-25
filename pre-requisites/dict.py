# Dictionary operations: get, update, pop, keys, etc.

book_info = {"title": "Advanced Python Programming", "author": "John Doe", "year": 2020}
print(f"Initial book info: {book_info}")

# adding new information to the dictionary
book_info["pages"] = 350
print(f"Book info after adding pages: {book_info}")

# getting an item with a fallback value
publisher = book_info.get("publisher", "Unknown")
print(f"Publisher: {publisher}")

# updating multiple fields in the dictionary
book_info.update({"publisher": "Tech Press", "edition": "2nd"})
print(f"Book info after update: {book_info}")

# removing an item using pop (for example, removing the edition)
removed_item = book_info.pop("edition")
print(f"Removed item: {removed_item}, Updated book info: {book_info}")

# retrieving keys and values
book_keys = book_info.keys()
book_values = book_info.values()
print(f"Book keys: {book_keys}")
print(f"Book values: {book_values}")

# using setdefault to provide a default if a key doesn't exist
pages = book_info.setdefault("pages", 0)
print(f"Pages (using setdefault): {pages}")
