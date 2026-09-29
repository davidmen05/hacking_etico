from flask import Flask
from main.routes import main_bp
from users.routes import users_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(users_bp)


if __name__ == '__main__':
    app.run(debug=True)