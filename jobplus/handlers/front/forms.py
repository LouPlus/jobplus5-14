from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, IntegerField
from wtforms.validators import Length, Email, EqualTo, DataRequired
from ..models import db, User, CompanyDetail, Job


class RegisterForm(FlaskForm):
    name = StringField('用户名', validators=[Length(4, 20, message="名字格式不符合要求！"),
                                          DataRequired(message="用户名不能为空！")])
    email = StringField('个人邮箱', validators=[Email(message="邮件格式错误！"),
                                            DataRequired(message="邮箱不能为空！")])
    passwd = PasswordField('密码', validators=[Length(6, 20, message="密码格式不正确！"),
                                             DataRequired(message="密码不能为空！")])
    repasswd = PasswordField(
        '重复密码',
        validators=[
            EqualTo(
                'passwd',
                message="两次输入的密码不一致！！")])
    submit = SubmitField('提交')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已注册过了！')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('该用户/企业 已经注册过了！')


class LoginForm(FlaskForm):
    email = StringField('个人邮箱', validators=[Email(message="邮件格式错误！"),
                                            DataRequired(message="邮箱不能为空！")])
    passwd = PasswordField('密码', validators=[Length(6, 20, message="密码格式不正确！"),
                                             DataRequired(message="密码不能为空！")])

    rememberme = BooleanField('记住我')

    submit = SubmitField('登录')
