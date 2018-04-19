from flask import render_template, url_for, request, abort, g, redirect, flash
from .forms import RegisterForm, LoginForm
from .import bp
from ..models import User, db
from flask_login import login_user, logout_user
# bp = Blueprint('front', __name__, template_folder="~/git/myproject/github/jobplus5-14/app/templates")


@bp.route('/')
def index():
    return render_template('front/index.html', active="index")


@bp.route('/login/<active>', methods=['GET', 'POST'])
def login(active):
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('front.index'))
    form = LoginForm()
    role = User.ROLE_JOBSEEKER
    if active == 'company':
        form.email.label = '企业邮箱'
        role = User.ROLE_COMPANY
    elif active == 'jobseeker':
        pass
    else:
        abort(404)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data, role=role).first()
        if user is not None and user.check_password(form.passwd.data):
            login_user(user, remember=form.rememberme.data)
            return redirect(url_for('front.index'))
        elif user is None:
            flash('用户名不存在或错误！')
            form.email.data = ''
        else:
            flash('密码错误！')
    return render_template('front/login.html', active=active, form=form)


@bp.route('/logout')
def logout():
    logout_user()
    flash('退出成功！')
    return render_template('front/index.html')


@bp.route('/register/<active>', methods=['GET', 'POST'])
def register(active):
    form = RegisterForm()
    if active == 'company':
        form.name.label = '企业名称'
        form.email.label = '企业邮箱'
    elif active == 'jobseeker':
        pass
    else:
        abort(404)
    if form.validate_on_submit():
        role = User.ROLE_JOBSEEKER
        if active == 'company':
            role = User.ROLE_COMPANY
        user = User(
            email=form.email.data,
            name=form.name.data,
            password=form.passwd.data, role=role)
        db.session.add(user)
        db.session.commit()
        flash('恭喜，注册成功！')
        return redirect(url_for('front.login', active='jobseeker'))
    return render_template('front/register.html', active=active, form=form)


@bp.route('/companies')
def companies():
    return render_template('front/companylist.html', active="companies")


@bp.route('/jobs')
def jobs():
    return render_template('front/joblist.html', active="jobs")


@bp.route('/jobseekers')
def jobseekers():
    return render_template('front/jobseekerlist.html', active="jobseekers")
