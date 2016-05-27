from application import app


@app.template_filter('condition')
def filter_condition(s):
    if s is dict:
        s = s.keys()[0].split('=')[1]
    if isinstance(s, unicode):
        return ' '.join(s.split('_'))
    return 'N/A'
