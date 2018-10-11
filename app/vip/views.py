from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from flask_login import current_user, login_required
from app.decorators import vip_required
from flask_rq import get_queue

from app import db

from app.vip.forms import *

from app.email import send_email

vip = Blueprint('vip', __name__)


@vip.route('/')
@login_required
@vip_required
def index():
    # "vip dashboard page."
    return render_template('vip/index.html')


@vip.route('/flow-count')
@login_required
@vip_required
def flow_count():
    return render_template('vip/flow_count.html')


# 次数统计
@vip.route('/times-count')
@login_required
@vip_required
def times_count():
    return render_template('vip/times_count.html')


# 时间统计
@vip.route('/duration-count')
@login_required
@vip_required
def duration_count():
    return render_template('vip/duration_count.html')
