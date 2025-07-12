from flask import Flask, render_template, request, redirect, url_for, session, flash
# from werkzeug.security import generate_password_hash, check_password_hash
# from database import init_db, add_user, get_user


app = Flask(__name__)
app.secret_key = ...
# init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(username, password)

        # user = get_user(username)
        # if user and check_password_hash(user[2], password):
        #     session['username'] = username
        #     flash('Вы успешно вошли в систему!', 'success')
        #     return redirect(url_for('home'))
        # else:
        #     flash('Неверное имя пользователя или пароль', 'danger')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(username, password)
        #
        # if get_user(username):
        #     flash('Это имя пользователя уже занято', 'danger')
        # else:
        #     add_user(username, password)
        #     flash('Регистрация прошла успешно! Теперь вы можете войти.', 'success')
        #     return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Вы вышли из системы', 'info')
    return redirect(url_for('home'))

@app.route('/account')
def account():
    return render_template('account.html')


if __name__ == "__main__":
    app.run(debug=True)
