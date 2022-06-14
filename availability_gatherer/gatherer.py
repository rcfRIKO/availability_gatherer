import re
import sqlite3
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from availability_gatherer.auth import login_required

from availability_gatherer.db import get_db

import uuid

bp = Blueprint('gatherer', __name__)

@bp.route('/')
def index():
    return render_template('gatherer/index.html')


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        print(type(start_date), start_date)
        error = None

        if not title:
            error = 'Title is required.'
        elif not start_date:
            error = 'Starting Date is required.'
        elif not end_date:
            error = 'Ending Date is required.'

        if error is None:
            gatherer_id = uuid.uuid4().hex
            db = get_db()
            db.execute(
                'INSERT INTO gatherer (uuid, creator_id, title, description, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?)',
                (gatherer_id, g.user['id'], title, description, start_date, end_date)
            )
            db.commit()
            return redirect(url_for('gatherer.view', id=gatherer_id))

        flash(error)
    
    return render_template('gatherer/create.html')


@bp.route('/view', methods=('GET', 'POST'))
def view():
    if request.args.get('id') is not None:
        gatherer_id = request.args.get('id')
        db = get_db()
        error = None

        gatherer = db.execute(
            'SELECT * FROM gatherer WHERE uuid = ?', (gatherer_id,)
        ).fetchone()

        if gatherer is None:
            error = 'Invalid ID.'
        else:
            return render_template('gatherer/view.html', gatherer=gatherer)

    flash(error)
    return redirect(url_for('gatherer.index'))
    
        
