from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, request, redirect, url_for, flash

from config import login_manager, app, db
from models import User
from forms import ContactForm


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = ContactForm()
    if form.validate_on_submit():
        nickname = form.nickname.data
        password = form.password.data

        user = User.query.filter_by(nickname=nickname).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Вы успешно вошли в систему!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Неверное имя пользователя или пароль', 'danger')
    else:
        # Если форма не прошла валидацию, ошибки доступны в form.errors
        if request.method == 'POST':
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Ошибка в поле {getattr(form, field).label.text}: {error}", 'error')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = ContactForm()
    if form.validate_on_submit():
        nickname = form.nickname.data
        password = form.password.data

        if User.query.filter_by(nickname=nickname).first():
            flash('Это имя пользователя уже занято', 'danger')
        else:
            user = User(nickname=nickname)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Регистрация прошла успешно! Теперь вы можете войти.', 'success')
            return redirect(url_for('login'))
    else:
        # Если форма не прошла валидацию, ошибки доступны в form.errors
        if request.method == 'POST':
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Ошибка в поле {getattr(form, field).label.text}: {error}", 'error')
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы', 'info')
    return redirect(url_for('index'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = ContactForm()
    if form.validate_on_submit():
        new_nickname = form.nickname.data
        new_password = form.password.data

        if new_nickname and new_nickname != current_user.nickname:
            if User.query.filter_by(nickname=new_nickname).first():
                flash('Этот никнейм уже занят', 'danger')
                return redirect(url_for('account'))
            current_user.nickname = new_nickname

        if new_password:
            current_user.set_password(new_password)

        db.session.commit()
        flash('Данные успешно обновлены', 'success')
        return redirect(url_for('account'))
    else:
        # Если форма не прошла валидацию, ошибки доступны в form.errors
        if request.method == 'POST':
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Ошибка в поле {getattr(form, field).label.text}: {error}", 'error')

    return render_template('account.html', form=form)

    # return render_template('account.html', user=current_user)


if __name__ == '__main__':
    app.run(debug=True)
