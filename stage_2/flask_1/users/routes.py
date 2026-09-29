from flask import Blueprint, render_template

users_bp = Blueprint('users', __name__)


@users_bp.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)