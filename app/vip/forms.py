# author:simzhangbest
from flask_wtf import Form
from wtforms import ValidationError
from wtforms.fields import (
    PasswordField,
    StringField,
    SubmitField,
)

from app import db
from app.models import Role, User
