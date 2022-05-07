from flask import Blueprint, render_template, request, flash, redirect, url_for,session
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import current_user,login_user,logout_user,login_required
from WebApp.db import dbconnection
from WebApp.db_functions import create_login_attempt_log,create_vistor_log
from WebApp.User_Class import userClass


auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():

    client_ip = request.remote_addr

    if request.method == 'POST':

        email = request.form.get('emaillogin')
        password = request.form.get('passwordlogin')

        dbconnect = dbconnection()

        dbconnect.execute('''
            SELECT email
            FROM users
            WHERE email = ?''', email)

        emailfromDB = dbconnect.fetchone()

        if emailfromDB:
            emailfromDBcheck = emailfromDB[0]
            ## Query here to grab hashed password
            dbconnect.execute('''
                                SELECT password,user_id
                                FROM users
                                WHERE email = ?;''', email)
            resultspass = dbconnect.fetchone()

            hashedpass = resultspass[0]
            if check_password_hash(hashedpass, password):

                create_login_attempt_log(emailfromDBcheck,client_ip,"T")

                session['loggedin'] = True
                session['user_id'] = resultspass[1]
                user_active = userClass(emailfromDBcheck)
                login_user(user_active)
                return redirect(url_for('views.home'))

            else:
                create_login_attempt_log(emailfromDBcheck, client_ip, "F")
                print("Incorrect Password!")


        else:
            create_login_attempt_log(email, client_ip, "F")
            print("Email Does not Exist")

    create_vistor_log(client_ip)

    # do I need user=current_user
    return render_template("login.html", user=current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))