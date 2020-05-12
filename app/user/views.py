# from flask import jsonify, request, url_for, redirect
# from flask_login import login_required, login_user, logout_user

# from . import user 
# from ..model import *


# @user.route('/register', methods=['GET', 'POST'])
# def register():
#     # User = User(email=request.form.get('email')
#     #             username=request.form.get('username')
#     #             first_name=request.form.get('first_name')
#     #             last_name=request.form.get('last_name')
#     #             password_hash=request.form.get('password')
#     #             address=request.form.get('address')
#     #             city=request.form.get('city')
#     #             state=request.form.get('state')
#     #             country=request.form.get('country')
#     #             phone=request.form.get('phone')
#     #              )
#     data= request.get_json()
#     User = User(email=data['email']
#                 username=data['username']
#                 first_name=data['first_name']
#                 last_name=data['last_name']
#                 password_hash=data['password']
#                 address=data['address']
#                 city=data['city']
#                 state=data['state']
#                 country=data['country']
#                 phone=data['phone']
# 	)
    
#     db.session.add(User)
#     db.session.commit()
    
#    return jsonify(User)


# @user.route('/login', methods=['GET', 'POST'])
# def login():
#     user_data=request.get_json()
    
#     User = User.query.filter_by(email=user_data['email']).first()
#         if employee is not None and employee.verify_password(
#                 user_data['password']):
#             # log User in
#             login_user(User)
#     		return True
#         else:
#             return False


# @user.route('/logout')
# @login_required
# def logout():
#     """
#     Handle requests to the /logout route
#     Log an employee out through the logout link
#     """
#     logout_user()

#     # redirect to the login page
#     return redirect(url_for(''))

