from flask import render_template
from flask_login import login_required

from app.chart import bp

@bp.route('/')
@login_required
def chart_list():
    return render_template('chart_list.html', title = 'List of Charts')

@bp.route('/book_ratings')
@login_required
def book_ratings_chart():
    # Route is empty for now, need to add code to create and return plot comparing book ratings
    return ''
    
@bp.route('/user_books')
@login_required
def user_books_chart():
    # Route is empty for now, need to add code to create and return plot comparing book ratings
    return ''
