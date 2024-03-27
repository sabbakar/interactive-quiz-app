from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/quiz_app_db'  # Update with your MySQL credentials and database name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# User model for SQLAlchemy
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Mock user authentication (replace with actual database query)
def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password_hash == password:
        return user
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = authenticate(username, password)
        if user:
            login_user(user)
            session['user_id'] = user.id
            return redirect(url_for('quiz'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html', error='')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('user_id', None)
    return redirect(url_for('login'))


# Your quiz route with login_required decorator
@app.route('/', methods=['GET', 'POST'])
@login_required
def quiz():
    # Your existing quiz logic here
    return render_template('quiz.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

