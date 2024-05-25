# main.py
import text_chunking
import model_summarization


def main():
    print("Welcome to the Document Processing System")
    input_path = input("Enter the path to the dataset folder: ")
    output_path = input("Enter the path to store chunked data: ")
    method = input("Choose the chunking method (chars, words, pages): ")
    if method == 'words':
        chunk_size = int(input("Enter chunk size in words: "))
        text_chunking.chunk_by_words(input_path, output_path, chunk_size)
    elif method == 'pages':
        text_chunking.chunk_by_pages(input_path, output_path)
    else:
        chunk_size = int(input("Enter chunk size in characters: "))
        text_chunking.chunk_by_chars(input_path, output_path, chunk_size)

    # Ensure the output file path is correct
    summary_output_path = input("Enter the path to store the summary output (include file name, e.g., summary.txt): ")
    model_name = input("Enter the model name for summarization (e.g., 't5-small'): ")
    summarizer = model_summarization.load_model(model_name)
    model_summarization.process_directory(output_path, summary_output_path, summarizer)


if __name__ == "__main__":
    main()

# Enter the path to the dataset folder: C:\Users\masen\PycharmProjects\RAG\dataset
# Enter the path to store chunked data: C:\Users\masen\PycharmProjects\RAG\chunked_dataset
# Choose the chunking method (chars, words, pages): words
# Enter chunk size in words: 1000
# Processed practitioners_guide_to_mlops_whitepaper.pdf into 10 chunks by words.
# Enter the model name for summarization (e.g., 't5-small'): t5-small
# Enter the path to store the summary output: C:\Users\masen\PycharmProjects\RAG\summary_dataset\summary.txt
