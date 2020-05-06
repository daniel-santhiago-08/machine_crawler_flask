from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import Length, Email, DataRequired

class LoginForm(FlaskForm):
    email = EmailField("E-mail", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(4,20,"O campo deve conter de 4 a 20 caracteres.")
    ])
    remember = BooleanField("Permanecer Conectado")
    submit = SubmitField("Logar")

class RegisterForm(FlaskForm):
    name = StringField("Nome Completo", validators=[
        DataRequired("O campo é obrigatório")
    ])
    email = EmailField("E-mail", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(4,20,"O campo deve conter de 4 a 20 caracteres.")
    ])
    submit = SubmitField("Cadastrar")

