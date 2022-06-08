from wtforms import Form, BooleanField, StringField, PasswordField, validators, EmailField, ValidationError


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)], render_kw={"autocomplete": "off"})
    email = EmailField('Email Address')
    first_name = StringField('first name', [validators.Length(min=3, max=120)])
    last_name = StringField('last name', [validators.Length(min=3, max=120)])
    course = StringField('course', [validators.Length(min=3, max=120)])
    university = StringField('university', [validators.Length(min=3, max=120)])

    def validate_username(self, field):
        from main import Student
        if Student.query.filter_by(username=field.data).first():
            raise ValidationError('username already exists')
