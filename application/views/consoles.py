from flask import render_template

from application import app, mongo


@app.route('/consoles/list')
def consoles_list():
    return render_template('consoles/list.html')
