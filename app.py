'''
    @Author Alvis Grigaļūns <alvisgrigaluns@gmail.com>
'''

from flask import Flask, render_template, url_for, redirect, request, session, flash
import MySQLdb

ufile = open('data/user.txt', 'r')
user = ufile.read()[:-1]
ufile.close()

pfile = open('data/password.txt', 'r')
password = pfile.read()[:-1]
pfile.close()

db = MySQLdb.connect("localhost", user, password, "checkbuy")

app = Flask(__name__)
app.secret_key = 'hello'


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
