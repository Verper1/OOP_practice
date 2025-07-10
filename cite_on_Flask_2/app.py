from flask import Flask, render_template  # request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/account')
def account():
    return render_template('account.html')


if __name__ == "__main__":
    app.run(debug=True)
