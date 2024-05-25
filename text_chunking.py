# text_chunking.py

import os
from PyPDF2 import PdfReader

def chunk_by_chars(input_path, output_path, chunk_size):
    """ Chunk text by a fixed number of characters. """
    for filename in os.listdir(input_path):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(input_path, filename)
            reader = PdfReader(file_path)
            full_text = ''
            for page in reader.pages:
                full_text += (page.extract_text() or '') + ' '

            chunks = [full_text[i:i + chunk_size] for i in range(0, len(full_text), chunk_size)]

            for i, chunk in enumerate(chunks):
                chunk_filename = f"{filename[:-4]}_chunk_{i}.txt"
                with open(os.path.join(output_path, chunk_filename), 'w', encoding='utf-8') as f:
                    f.write(chunk)
            print(f"Processed {filename} into {i+1} chunks by characters.")

def chunk_by_words(input_path, output_path, chunk_size):
    """ Chunk text by a fixed number of words. """
    for filename in os.listdir(input_path):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(input_path, filename)
            reader = PdfReader(file_path)
            full_text = ''
            for page in reader.pages:
                full_text += (page.extract_text() or '') + ' '

            words = full_text.split()
            chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

            for i, chunk in enumerate(chunks):
                chunk_filename = f"{filename[:-4]}_chunk_{i}.txt"
                with open(os.path.join(output_path, chunk_filename), 'w', encoding='utf-8') as f:
                    f.write(chunk)
            print(f"Processed {filename} into {i+1} chunks by words.")

def chunk_by_pages(input_path, output_path):
    """ Chunk text by pages. """
    for filename in os.listdir(input_path):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(input_path, filename)
            reader = PdfReader(file_path)

            for i, page in enumerate(reader.pages):
                text = page.extract_text() or ''
                chunk_filename = f"{filename[:-4]}_chunk_{i}.txt"
                with open(os.path.join(output_path, chunk_filename), 'w', encoding='utf-8') as f:
                    f.write(text)
            print(f"Processed {filename} into {i+1} chunks by pages.")
