from flask import Flask, request, render_template

app = Flask(__name__, root_path='Frontend')

@app.route('/' , methods=['GET', 'POST'])
def my_form():
    return render_template('Main.html')

@app.route('/', methods=['POST'])
def my_form_post():
    if request.method == 'POST': 
        text = request.form['input_text']
        processed_text = text.upper()+"yolo"
        return render_template('Main.html', result = processed_text )

if __name__ == '__main__':
    app.run()