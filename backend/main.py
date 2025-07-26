from flask import Flask
from flask_cors import CORS

from extensions import db, jwt, bcrypt

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db.init_app(app)
jwt.init_app(app)
bcrypt.init_app(app)

from routes.auth import auth_bp
from routes.sessions import sessions_bp

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(sessions_bp, url_prefix="/api/sessions")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
