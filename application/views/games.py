from flask import render_template, request
from pymongo import ASCENDING
from bson import ObjectId

from application import app, mongo
from application.forms import GameListSortForm


def games_per_console():
    consoles = {}
    for game in mongo.db.games.find():
        # platform = game['platform'][:game['platform'].find('[')].rstrip()
        platform = game['platform']
        if platform in consoles:
            consoles[platform] += 1
        else:
            consoles[platform] = 1
    return consoles


@app.route('/games/consoles')
def games_by_console():
    return render_template('games/consoles.html', games=games_per_console())


@app.route('/games/list', methods=['POST', 'GET'])
def games_list():
    form = GameListSortForm()
    consoles = games_per_console()
    form.system.choices = sorted([(i, i) for i in consoles.keys()])

    if form.validate_on_submit():
        all_games = mongo.db.games.find({'platform': form.system.data}).sort(
            'name', ASCENDING)
    else:
        all_games = mongo.db.games.find().sort('name', ASCENDING)

    return render_template('games/list.html',
                           consoles=consoles,
                           all_games=all_games,
                           form=form)


@app.route('/games/<id>/detail')
def game_detail(id):
    game = mongo.db.games.find_one({'_id': ObjectId(id)})
    return render_template('games/detail.html', game=game)
