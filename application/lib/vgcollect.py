import requests

API_BASE_URL = 'http://api.vgcollect.com/'
API_KEY = 'abcdefg'


def search_items(args):
    r = requests.get('/'.join([API_BASE_URL, 'search', '+'.join(args),
                               API_KEY]))
    if r.status_code == 200 and len(r.json()):
        return r.json()
    else:
        return None


def get_item(item_id):
    r = requests.get('/'.join([API_BASE_URL, 'items', item_id, API_KEY]))
    if r.status_code == 200 and len(r.json()):
        return r.json()['results']
