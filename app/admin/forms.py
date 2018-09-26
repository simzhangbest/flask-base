from flask_wtf import Form
from wtforms import ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields import (
    PasswordField,
    StringField,
    SubmitField,
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import (
    Email,
    EqualTo,
    InputRequired,
    Length,
)

from app import db
from app.models import Role, User


class ChangeUserEmailForm(Form):
    email = EmailField(
        '新邮箱', validators=[InputRequired(),
                                 Length(1, 64),
                                 Email()])
    submit = SubmitField('更新邮箱')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')


class ChangeAccountTypeForm(Form):
    role = QuerySelectField(
        '新的账号类型',
        validators=[InputRequired()],
        get_label='name',
        query_factory=lambda: db.session.query(Role).order_by('permissions'))
    submit = SubmitField('更新账号')


class InviteUserForm(Form):
    role = QuerySelectField(
        '账号类型',
        validators=[InputRequired()],
        get_label='name',
        query_factory=lambda: db.session.query(Role).order_by('permissions'))
    first_name = StringField(
        '姓', validators=[InputRequired(),
                                  Length(1, 64)])
    last_name = StringField(
        '名', validators=[InputRequired(),
                                 Length(1, 64)])
    email = EmailField(
        '邮箱', validators=[InputRequired(),
                             Length(1, 64),
                             Email()])
    submit = SubmitField('邀请')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册')


class NewUserForm(InviteUserForm):
    password = PasswordField(
        '密码',
        validators=[
            InputRequired(),
            EqualTo('password2', 'Passwords must match.')
        ])
    password2 = PasswordField('确认密码', validators=[InputRequired()])

    submit = SubmitField('创建')
