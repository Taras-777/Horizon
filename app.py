from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration.html')
def registration():
    return render_template('registration.html')


@app.route('/home.html')
def login():
    return render_template('home.html')


@app.route('/statistics.html')
def statistics():
    return render_template('statistics.html')


if __name__ == "__main__":
    app.run(debug=True)
