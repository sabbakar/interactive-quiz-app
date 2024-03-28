from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:SASbubakar2004@localhost/quiz_app_db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password_hash== password:
        return user  # Successful authentication
    return None  # Invalid credentials

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

@app.route('/', methods=['GET', 'POST'])
@login_required
def quiz():
     current_question = fetch_current_question()  # Fetch the current question 
     return render_template('quiz.html', current_question=current_question)

if __name__ == '__main__':
    app.run(debug=True)
