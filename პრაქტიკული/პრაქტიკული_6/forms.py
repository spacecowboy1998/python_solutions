from wtforms import Form,StringField, validators, EmailField, ValidationError,FileField


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)], render_kw={"autocomplete": "off"})
    email = EmailField('Email Address')
    first_name = StringField('First Name', [validators.Length(min=3, max=120)])
    last_name = StringField('Last Name', [validators.Length(min=3, max=120)])
    course = StringField('Course', [validators.Length(min=3, max=120)])
    university = StringField('University', [validators.Length(min=3, max=120)])

    def Validate_username(self, field):
        from main import Student
        if Student.query.filter_by(username=field.data).first():
            raise ValidationError('username already exists')

    def Validate_email(self, field):
        from main import Student
        if Student.query.filter_by(email=field.data).first():
            raise ValidationError('username already exists')