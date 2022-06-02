from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # ამის დაწერის შემდეგ აღარ არის საჭირო რომ ვაკომიტოთ
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    Semester = db.Column(db.Integer, nullable=False)
    GPA = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    return redirect('/user/')


@app.route('/user/add', methods=['GET'])
def user_add():
    return render_template('create.html')


@app.route('/user/<user_id>/', methods=['GET', 'PUT', 'DELETE'])
@app.route('/user/', methods=['GET', 'POST'])
def user_crud(user_id=None):
    method = request.method
    if method == 'GET':
        data = {
            "students": Student.query.all()
                }
        return render_template('users.html', **data)
    if method == 'POST':
        first_name = request.form.get('firstname')
        semester = request.form.get('Semester')
        gpa = request.form.get('GPA')
        student = Student(first_name=str(first_name), Semester=int(semester), GPA=int(gpa))
        db.session.add(student)
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
