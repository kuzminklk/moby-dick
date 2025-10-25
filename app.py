from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chapter-<int:chapterNumber>')
def chapter(chapterNumber):
    return render_template(f'chapters/chapter-{chapterNumber}.html')

if __name__ == '__main__':
    app.run(debug=True)