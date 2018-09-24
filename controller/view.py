# coding=utf-8
'some comment...'
from flask import render_template, redirect

from common.exception import ServiceException
from common.token_util import decode_email_token
from service.auth_service import AuthService

__author__ = 'Jiateng Liang'

from bootstrap_init import app


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/verify')
def verify_page():
    return render_template('verify.html')


@app.route('/register/<username>')
def register_page(username):
    username = decode_email_token(username)
    account = AuthService.get_account_by_username(username)
    if account.confirmed:
        return redirect('/login')
    return render_template('register.html')


@app.route('/')
def index_page():
    return render_template('home.html')
