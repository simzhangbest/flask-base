from flask import url_for
from flask_wtf import Form
from wtforms import ValidationError
from wtforms.fields import (
    BooleanField,
    PasswordField,
    StringField,
    SubmitField,
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length

from app.models import User


class LoginForm(Form):
    email = EmailField(
        '邮箱', validators=[InputRequired(message="此处不能为空"),
                             Length(1, 64),
                             Email(message="无效的邮箱地址")])
    password = PasswordField('密码', validators=[InputRequired(message="此处不能为空")])
    remember_me = BooleanField('保持登录状态')
    submit = SubmitField('登录')


class RegistrationForm(Form):
    first_name = StringField(
        '姓', validators=[InputRequired(message="此处不能为空"),
                                  Length(1, 64)])
    last_name = StringField(
        '名', validators=[InputRequired(message="此处不能为空"),
                                 Length(1, 64)])
    email = EmailField(
        '邮箱', validators=[InputRequired(message="此处不能为空"),
                             Length(1, 64),
                             Email(message="无效的邮箱地址")])
    password = PasswordField(
        '密码',
        validators=[
            InputRequired(message="此处不能为空"),
            EqualTo('password2', '两次输入的密码须保持一致！')
        ])
    password2 = PasswordField('确认密码', validators=[InputRequired(message="此处不能为空")])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经注册. (需要直接'
                                  '<a href="{}">登录</a> 吗?)'.format(
                                    url_for('account.login')))


class RequestResetPasswordForm(Form):
    email = EmailField(
        '邮箱', validators=[InputRequired(message="此处不能为空"),
                             Length(1, 64),
                             Email(message="无效的邮箱地址")])
    submit = SubmitField('重设密码')

    # We don't validate the email address so we don't confirm to attackers
    # that an account with the given email exists.


class ResetPasswordForm(Form):
    email = EmailField(
        '邮箱', validators=[InputRequired(message="此处不能为空"),
                             Length(1, 64),
                             Email(message="无效的邮箱地址")])
    new_password = PasswordField(
        '新密码',
        validators=[
            InputRequired(message="此处不能为空"),
            EqualTo('new_password2', '两次输入的密码须保持一致！')
        ])
    new_password2 = PasswordField(
        '确认新密码', validators=[InputRequired(message="此处不能为空")])
    submit = SubmitField('重设密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('无效的邮箱地址')


class CreatePasswordForm(Form):
    password = PasswordField(
        '密码',
        validators=[
            InputRequired(message="此处不能为空"),
            EqualTo('password2', '两次输入的密码须保持一致！')
        ])
    password2 = PasswordField(
        '确认新密码', validators=[InputRequired(message="此处不能为空")])
    submit = SubmitField('设置密码')


class ChangePasswordForm(Form):
    old_password = PasswordField('老密码', validators=[InputRequired(message="此处不能为空")])
    new_password = PasswordField(
        '新密码',
        validators=[
            InputRequired(message="此处不能为空"),
            EqualTo('new_password2', '两次输入的密码须保持一致！')
        ])
    new_password2 = PasswordField(
        '确认新密码', validators=[InputRequired(message="此处不能为空")])
    submit = SubmitField('更新密码')


class ChangeEmailForm(Form):
    email = EmailField(
        '新邮箱', validators=[InputRequired(message="此处不能为空"),
                                 Length(1, 64),
                                 Email(message="无效的邮箱地址")])
    password = PasswordField('Password', validators=[InputRequired(message="此处不能为空")])
    submit = SubmitField('更新邮箱')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经注册')
