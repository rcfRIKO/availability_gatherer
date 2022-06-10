import sqlite3
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from availability_gatherer.db import get_db

import uuid

bp = Blueprint('gatherer', __name__)

@bp.route('/')
def index():
    return render_template('gatherer/index.html')

@bp.route('/gatherer', methods=['GET', 'POST'])
def gatherer():
    db = get_db()
    if request.method == 'GET':
        return request.args.get('id')
    elif request.method == 'POST':
        id = uuid.uuid4()
        try:
            cursor = db.execute(
            'INSERT INTO gatherers (gatherer_id, title, description, start_date, end_date)'
            'VALUES (?, ?, ?, ?, ?);',
            (id, request.form.get('title'), request.form.get('description'), request.form.get('start_date'), request.form.get('end_date')))
        except sqlite3.Error as e:
            flash(e)
            redirect(url_for('gatherer.index'))
        else:
            redirect(url_for('gatherer.gatherer', id=uuid))


