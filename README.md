
# Document Processing and Summarization System

## Overview

This project is a Document Processing and Summarization System designed to handle PDFs by chunking them into smaller segments and then summarizing these segments using a Hugging Face model. The project is structured to allow for easy modification and extension.

## Project Structure

- `main.py` - The main script that orchestrates the entire process.
- `text_chunking.py` - Handles the chunking of PDF documents into smaller text files.
- `model_summarization.py` - Loads a summarization model from Hugging Face and processes text files to generate summaries.
- `README.md` - This file, providing an overview and instructions for the project.

## Requirements

- Python 3.7 or higher
- Pip (Python package installer)

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/MSenhoury/document-processing-summarization.git
   cd document-processing-summarization
   ```

2. **Create a virtual environment** (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
   ```

3. **Install the required packages**:

   ```sh
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not provided, install the dependencies manually:

   ```sh
   pip install PyPDF2 transformers
   ```

## Usage

### Chunking PDF Documents (UI1)

1. **Run `main.py`**:

   ```sh
   python main.py
   ```

2. **Follow the prompts**:

   - Enter the path to the dataset folder containing PDF files.
   - Enter the path to store the chunked text files.
   - Choose the chunking method (`chars`, `words`, `pages`).
   - If you chose `chars` or `words`, you will be prompted to enter the chunk size.

### Summarizing Text Files (UI2)

After chunking, the script will automatically proceed to summarization:

1. **Enter the model name** for summarization (e.g., `t5-small`).
2. **Enter the path to store the summary output**, including the file name (e.g., `summary.txt`).

The script will process each chunked text file and generate a summary for each, then combine these summaries into a single output file.

## File Descriptions

### `main.py`

The main entry point of the project. It guides the user through the steps of chunking PDF documents and summarizing the resulting text files.

### `text_chunking.py`

Contains functions for chunking PDF documents:

- `chunk_by_chars(input_path, output_path, chunk_size)` - Chunks text by a fixed number of characters.
- `chunk_by_words(input_path, output_path, chunk_size)` - Chunks text by a fixed number of words.
- `chunk_by_pages(input_path, output_path)` - Chunks text by individual pages.

### `model_summarization.py`

Contains functions for summarizing text files using a Hugging Face model:

- `load_model(model_name)` - Loads the specified summarization model.
- `summarize_text(summarizer, file_path)` - Generates a summary for the text in the specified file.
- `process_directory(directory_path, output_file_path, summarizer)` - Processes all text files in a directory and writes their summaries to a single output file.

## Notes

- Ensure that the paths you provide for input and output are correct and that you have write permissions for the output directory.
- The summarization step may take some time depending on the size of the text and the model used.
- For very large documents, consider chunking by pages or by a manageable number of words to avoid exceeding the model's input limits.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
