from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def panel():
    return render_template("panel.html")


@main_bp.route('/inicio')
def home():
    return render_template("index.html")