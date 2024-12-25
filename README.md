# Project Overview

This project contains scripts that split and process large text files, such as PDFs and plain text, into smaller chunks. It also includes utility functions for working with different data types like strings, lists, and dictionaries.

## Prerequisites

### dict.py
Demonstrates basic operations with Python dictionaries, such as adding, updating, and retrieving values, and handling dictionary keys.

### tuple.py
Shows how to work with Python tuples, including counting occurrences, indexing, and concatenation of tuples.

### list.py
Provides examples of list operations, including appending, extending, removing items, sorting, and using list comprehensions.

### strings.py
Illustrates string manipulation techniques like encoding, decoding, stripping, splitting, and formatting strings for paths or messages.

### intgers.py
Covers integer operations, such as arithmetic, division, absolute values, and bitwise operations.

## Chunks

### 01_string_chunk_creator_to_chunk.py
This script splits a given string into smaller chunks based on a specified chunk size. It is helpful for splitting large documents into manageable pieces.

### 02_paragraph_chunk_creator_to_chunk.py
This file reads a text file, splits the content by paragraphs, and then splits those paragraphs into smaller chunks.

### 03_text_file_chunk_creator_to_chunk.py
This script processes a text file, breaking it into chunks of a specified size. It handles large files, ensuring each chunk does not exceed a given size.

### 04_pdf_page_chunk_creator_to_chunk.py
This script processes a PDF file, splitting the content into chunks based on individual pages. It helps when working with PDF documents.

### 05_read_pages_pdf_to_chunk.py
This file reads and processes specific pages of a PDF, creating chunks from the selected pages. Useful for processing parts of large PDF documents.

### 06_chunk_util.py
This utility file provides helper functions for working with text chunks, including chunking with overlap to ensure smooth transitions between chunks.
