from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)


@app.route('/')
def hello_there():
    return render_template("index.html")

@app.route('/index')
def comp():
    return render_template("index.html")

@app.route('/search')
def sear():
    return render_template("search.html")

@app.route('/trend')
def tren():
    return render_template("trend.html")
if __name__ == "__main__":
    app.run(debug=True, port=8080)