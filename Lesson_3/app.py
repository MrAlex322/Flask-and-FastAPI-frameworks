from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = '#d$lcc$r8w0r&(sb-9y-h2&6$imewpycn8pyq+*4yv4^w38)6b'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


@app.route('/')
def authorization():
    user_name = session.get('user_name')
    return render_template('authorization.html', user_name=user_name)


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "Пользователь с таким email уже существует!"

        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return f"Привет, {first_name}"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
