# Integer operations: addition, subtraction, division, etc.

num_pages = 250
pages_read = 90
pages_left = num_pages - pages_read
print(f"Pages left to read: {pages_left}")

# performing division and integer division
division_result = num_pages / 7
integer_division_result = num_pages // 7
print(f"Floating-point division: {division_result}")
print(f"Integer division: {integer_division_result}")

# absolute value (useful when counting remaining pages in a document)
remaining_pages = -20
print(f"Absolute remaining pages: {abs(remaining_pages)}")

# bitwise operations on page numbers
even_page_check = num_pages & 1
print(f"Checking if num_pages is even (bitwise AND): {even_page_check == 0}")
