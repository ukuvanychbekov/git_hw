from flask import request, render_template, redirect, url_for, flash
from . import db
from . import models


# post functions


def index():
    file = models.Transactions.query.all()
    return render_template('index_card.html', file=file)

def transactions_add():
    period = request.args.get('period')
    value = request.args.get('value')
    status = request.args.get('status')
    unit = request.args.get('unit')
    subject = request.args.get('subject')
    new_transaction = models.Transactions(period=period, value=value, status=status, unit=unit, subject=subject)
    db.session.add(new_transaction)
    db.session.commit()
    return redirect(url_for('index'))


