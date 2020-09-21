from flask import Flask, request, render_template
from text_summarizer import read_article, sentence_similarity, build_similarity_matrix, generate_summary

app = Flask(__name__, root_path='D:\\Projects\\Text_summarizer\\Frontend', static_folder='D:\\Projects\\Text_summarizer\\Frontend\\static')

@app.route('/' , methods=['GET'])
def my_form():
    return render_template('Main.html')

@app.route('/', methods=['POST'])
def my_form_post():
    if request.method == 'POST': 
        text = request.form['input_text']
        final_text = generate_summary(text)
        return render_template('Main.html', result = final_text, input = text )

if __name__ == '__main__':
    app.run()