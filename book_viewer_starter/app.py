from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    with open('book_viewer/data/toc.txt') as file:
        contents = file.readlines()
    return render_template('home.html', contents=contents)

@app.route("/chapters/1")
def chapter_1():
    chapter_title = "Chapter 1"
    with open('book_viewer/data/toc.txt', 'r') as file:
        contents = file.readlines()
    with open('book_viewer/data/chp1.txt', 'r') as file:
        chapter = file.read()
    return render_template('chapter.html',
                           chapter_title=chapter_title,
                           contents=contents,
                           chapter=chapter)

if __name__ == "__main__":
    app.run(debug=True, port=5003)