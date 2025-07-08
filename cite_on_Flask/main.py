from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.title


@app.route('/', methods=['POST', 'GET'])
def index():
    notes = Notes.query.all()

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        note = Notes.query.filter_by(title=title, description=description).first()

        try:
            db.session.delete(note)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f'Ошибка: {e}'
    else:
        return render_template('index.html', data=notes)


@app.route('/login_adm_page', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        # Здесь должна быть логика аутентификации
        # Если аутентификация прошла успешно, перенаправляем на /admin_panel
        return redirect(url_for('admin_panel'))
    # Если GET запрос, показываем форму входа
    return render_template('login_adm_page.html')

# страница админ панели
@app.route('/admin_panel')
def admin_panel():
    # Загрузка и отображение админ-панели
    return render_template('admin_panel.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST', 'GET'])
def crate():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        note = Notes(title=title, description=description)

        try:
            db.session.add(note)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f'Ошибка: {e}'
    else:
        return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)
