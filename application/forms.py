from flask.ext.wtf import Form
from wtforms.fields import SelectField, SubmitField, TextField
from wtforms.validators import Required


class SearchForm(Form):
    query = TextField('Query', validators=[Required()])

    submit = SubmitField('Search')


class GameListSortForm(Form):
    system = SelectField('System')

    submit = SubmitField('Filter')
