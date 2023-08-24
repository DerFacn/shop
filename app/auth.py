from flask import Blueprint, jsonify, request, redirect, url_for, session
from .db import get_db
from werkzeug.security import generate_password_hash, check_password_hash


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    password = request.form['password']
    error = None
    db = get_db()
    if error is None:
        try:
            db.execute(
                'INSERT INTO user (email, password) VALUES (?, ?)',
                (email, generate_password_hash(password))
            )
            db.commit()
        except db.IntegrityError:
            error = 'Email is already registered!'
        else:
            return redirect(url_for('auth.login'))
    return jsonify(error=error)


@bp.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    error = None
    db = get_db()
    user = db.execute(
        'SELECT * FROM user WHERE email = ?', (email,)
    ).fetchone()

    if user is None:
        error = 'Incorrect username.'
    elif not (check_password_hash(user['password'], password)):
        error = 'Incorrect password'

    if error is None:
        session.clear()
        session['user_id'] = user['id']
        return redirect(url_for('index'))
    return jsonify(error=error)
