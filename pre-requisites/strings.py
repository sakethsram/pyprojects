# String manipulations (encode, strip, decode, split, join, replace, etc.)

document_title = "  My Awesome PDF File!   "

# encoding string to bytes
encoded_title = document_title.encode('utf-8')
print(f"Encoded document title: {encoded_title} ({type(encoded_title)})")

# stripping spaces from both sides
cleaned_title = document_title.strip()
print(f"Cleaned title (stripped): '{cleaned_title}'")

# decoding bytes back into a string
decoded_title = encoded_title.decode('utf-8')
print(f"Decoded title: '{decoded_title}'")

# splitting the title by space
split_title = document_title.split(" ")
print(f"Split title: {split_title}")

# joining the words with a hyphen
joined_title = "-".join(split_title)
print(f"Joined title: '{joined_title}'")

# replacing a substring
replaced_title = document_title.replace("Awesome", "Great")
print(f"Replaced title: '{replaced_title}'")

# using strip, decode, join in practical example (path processing)
file_path = "/home/user/docs/My Awesome PDF File.pdf"
file_name = "/".join(file_path.split("/")[:-1])  # join all parts of the path except the last part
print(f"File path excluding file name: '{file_name}'")

# formatting title with placeholders
formatted_message = "File name: {}, located at {}".format(cleaned_title, file_name)
print(f"Formatted message: '{formatted_message}'")
