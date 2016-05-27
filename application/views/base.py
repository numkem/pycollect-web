from flask import render_template

from application import app, mongo
from application.forms import SearchForm
from application.lib.vgcollect import search_items


@app.route('/')
def index():
    return render_template('index.html')


def merge_results(db_games, api_games):
    games = {g['id']: g for g in db_games}
    for item in api_games:
        if item['game_id'] not in games:
            # Fixes for API object returned from search function
            item['condition'] = 'Not Owned'
            item['platform'] = item['category_name']
            item['id'] = item['game_id']
            games[item['game_id']] = item
    return games.values()


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()

    if form.validate_on_submit():
        # Get games from current database
        api_games = search_items(form.query.data.split(' '))

        # Get games from API
        db_games = mongo.db.games.find({'$text': {'$search': form.query.data}})
        search_results = merge_results(list(db_games), api_games)
        return render_template('search.html',
                               form=form,
                               results=search_results)
    return render_template('search.html', form=form, results=None)
