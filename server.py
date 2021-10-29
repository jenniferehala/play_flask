from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")


@app.route('/play')
def play_page():
    return render_template("play_3.html", num=3, )

@app.route('/play/<int:num>')
def boxes_repeat(num):
    return render_template("play_3.html", num=num, color="lightblue")

@app.route('/play/<int:num>/<string:color>')
def boxes_repeat2(num, color):
    return render_template("play_3.html", num=num, color=color)


if __name__=="__main__":
    app.run(debug=True) 