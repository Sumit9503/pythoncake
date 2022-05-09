from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/user-login', methods=['GET','POST'])
def user_login():
    data = request.form
    print(data)
    return render_template("user_login.html")

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account Created!', category='success')
    return render_template("sign_up.html")

@auth.route('/admin-login', methods=['GET','POST'])
def admin_login():
    data = request.form
    print(data)
    return render_template("admin_login.html")
