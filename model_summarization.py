# model_summarization.py

from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import os


def load_model(model_name="t5-small"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return pipeline("summarization", model=model, tokenizer=tokenizer)


def summarize_text(summarizer, file_path, max_length=512):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        text = file.read()
    # Tronquer le texte si nécessaire
    if len(text) > max_length:
        text = text[:max_length]  # Simple truncation to max_length characters
    return summarizer(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']


def process_directory(directory_path, output_file_path, summarizer):
    summaries = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            print(f"Summarizing {filename}...")
            summary = summarize_text(summarizer, file_path)
            # Append only the summary text
            summaries.append(f"{summary}\n\n")  # Remove filename from output

    # Make sure the output directory exists
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # Write all summaries into a single file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(summaries)
    print(f"All summaries have been written to {output_file_path}")

