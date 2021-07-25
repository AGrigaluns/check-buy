'''
    @Author Alvis Grigaļūns <alvisgrigaluns@gmail.com>
'''

from flask import Flask, render_template, url_for, redirect, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello'

# ===========================> Base page
@app.route('/')
def homepage():
    return render_template('base.html')

# ===========================> Shop page
@app.route('/products')
def products():
    return render_template('products.html')

# ===========================> Manufactures page
@app.route('/manufactures')
def manufactures():
    return render_template('manufactures.html')

# ===========================> Contacts page
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# ===========================> About page
@app.route('/about')
def about():
    return render_template('about.html')

# ===========================> Handling user login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
       user = request.form['email']
       user = request.form['password']
       session['user'] = user
       return redirect(url_for('user'))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template('login.html')

# ===========================> Profile page for user data
@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for('login'))

# ===========================> Handle user logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# ===========================> Run app
if __name__ == '__main__':
    app.run(debug=True)
