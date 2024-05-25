from flask import Flask, render_template, request, redirect, url_for
import text_chunking
import model_summarization
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_path = request.form['input_path']
        output_path = request.form['output_path']
        method = request.form['method']
        chunk_size = int(request.form['chunk_size']) if 'chunk_size' in request.form else None

        if method == 'words':
            text_chunking.chunk_by_words(input_path, output_path, chunk_size)
        elif method == 'pages':
            text_chunking.chunk_by_pages(input_path, output_path)
        else:
            text_chunking.chunk_by_chars(input_path, output_path, chunk_size)

        # Prepare summarization
        summary_output_path = request.form['summary_output_path']
        model_name = request.form['model_name']
        summarizer = model_summarization.load_model(model_name)
        model_summarization.process_directory(output_path, summary_output_path, summarizer)

        return redirect(url_for('summary', path=summary_output_path))

    return render_template('index.html')


@app.route('/summary')
def summary():
    summary_path = request.args['path']
    with open(summary_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return render_template('summary.html', summary_content=content)


if __name__ == '__main__':
    app.run(debug=True)
