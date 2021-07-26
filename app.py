'''
    @Author Alvis Grigaļūns <alvisgrigaluns@gmail.com>
'''

from flask import Flask, render_template, url_for, redirect, request, session, flash
import MySQLdb
from flask_login import UserMixin

app = Flask(__name__)
app.secret_key = 'hello'


# =============================================================> Database user class
# class Note(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # data = db.Column(db.String(1000))
    # date = db.Column(db.DateTime(timezone=True), default=func.now())



# class User(db.Model, UserMixin):
    # id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(150), unique=True)
    # password = db.Column(db.String(150))
    # name = db.Column(db.String(150))


# =============================================================> Navigation
@app.route('/')
def homepage():
    return render_template('base.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/manufactures')
def manufactures():
    return render_template('manufactures.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


# =============================================================> Registration, login, logout, user profile
# ===========================> Handling user login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
       user = request.form['email']
       session['user'] = user
       return redirect(url_for('user'))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template('login.html')


# ===========================> Handle user logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


# ============================> Handle registration
@app.route('/register', methods=['POST', 'GET'])
def register():
    '''
    if request.method == "POST":
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('That is not a valid email!', category='error')
        elif len(name) < 2:
            flash('Your name is to short', category='error')
        elif password1 != password2:
            flash('Passwords dont match', category='error')
        elif len(password1) < 7:
            flash('Your password is too short!', category='error')
        else:
            flash('Great! You are successfully registered!', category='success')
            '''
    return render_template('register.html')


# ===========================> Profile page for user data
@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for('login'))


# ===========================> Run app
if __name__ == '__main__':
    app.run(debug=True)
