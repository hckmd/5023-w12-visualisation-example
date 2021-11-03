import json

from flask import render_template
from flask_login import login_required
import pandas as pd
import plotly.express as px
import plotly

from app.chart import bp
from app.models import Book

@bp.route('/')
@login_required
def chart_list():
    return render_template('chart_list.html', title = 'List of Charts')

@bp.route('/book_ratings')
@login_required
def book_ratings_chart():
    # Retrieve all the books in the collection
    book_query = Book.query
    df = pd.read_sql(book_query.statement, book_query.session.bind)

    # Draw the chart and dump it in JSON format
    chart = px.bar(df, x='title', y='critics_rating')
    chart_JSON = json.dumps(chart, cls= plotly.utils.PlotlyJSONEncoder, indent=4)

    # Returns the template, including the JSON data for the chart
    return render_template('chart_page.html', title = 'Critic ratings for books', chart_JSON = chart_JSON)
    
@bp.route('/user_books')
@login_required
def user_books_chart():
    # Route is empty for now, need to add code to create and return plot comparing book ratings
    return ''
