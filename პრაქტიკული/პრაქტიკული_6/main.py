import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from forms import RegistrationForm

base_dir = os.path.abspath(os.path.dirname(__file__))

upload_dir = os.path.join(base_dir, 'uploads')
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students_db.sqlite3'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # ამის დაწერის შემდეგ აღარ არის საჭირო რომ ვაკომიტოთ
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    course = db.Column(db.String(32), nullable=False)
    university = db.Column(db.String(32), nullable=False)
    avatar = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/user/add', methods=['GET'])
def user_add():
    form = RegistrationForm()
    return render_template('create.html', form=form)


@app.route('/user/update/<user_id>', methods=['GET'])
def user_update(user_id):
    user = Student.query.get(user_id)
    form = RegistrationForm(obj=user)
    return render_template('create.html', form=form)


@app.route('/user/<user_id>/', methods=['GET', 'PUT', 'DELETE'])
@app.route('/', methods=['GET', 'POST'])
def user_crud(user_id=None):
    method = request.method
    if method == 'GET':
        data = {
            "students": Student.query.all()
        }
        return render_template("users.html", data=data)

    if method == 'POST':
        form = RegistrationForm(request.form)
        if form.validate():
            avatar = request.files['avatar']
            if avatar:
                avatar.save(f'{upload_dir}/{avatar.filename}')
                student = Student(
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    username=form.username.data,
                    university=form.university.data,
                    course=form.course.data,
                    avatar=avatar.filename
                )
                db.session.add(student)
            return redirect(url_for('user_crud'))
        return render_template("create.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
