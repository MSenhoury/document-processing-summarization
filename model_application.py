from transformers import pipeline
import os


def load_and_apply_model(model_name, directory_path, use_gpu=False):
    device = 0 if use_gpu else -1  # specifying device; 0 for GPU and -1 for CPU
    classifier = pipeline('text-classification', model=model_name, device=device)

    results = {}
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8', errors='replace') as file:  # Handle decoding errors
                text = file.read()
                try:
                    result = classifier(text)
                    results[filename] = result
                except Exception as e:
                    results[filename] = str(e)

    return results
