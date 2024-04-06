from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count_words', methods=['POST'])
def count_words():
    text = request.form['text']
    word_count = {}
    words = text.split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return jsonify(word_count)

if __name__ == '__main__':
    app.run()
