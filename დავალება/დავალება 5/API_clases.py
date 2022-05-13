import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'


def get_data(url, **params):
    res = requests.get(f'{BASE_URL}/{url}', params=params)
    if res.status_code == 200:
        return res.json()
    return []


class User:
    def __init__(self, user_id, pk, title, body):
        self._id = pk
        self._user_id = user_id
        self._title = title
        self._body = body

    def get_values(self):
        return [self._user_id, self._id, self._title, self._body]


class Todos:

    def __init__(self, user_id, pk, title, compl):
        self._user_id = user_id
        self._id = pk
        self._title = title
        self._completed = compl

    def as_json(self):
        return {
            'user_id': self._user_id,
            'id': self._id,
            'title': self._title,
            'completed': self._completed
        }

    def get_values(self):
        return [self._user_id, self._id, self._title, self._completed]


# posts = get_data('posts')
# post_objects = [Post(p['userId'], p['id'], p['title'], p['body']) for p in posts]
# pprint(post_objects[0].as_json())

# todos = get_data("todos")
# todo_objects = [Todos(d['userId'], d['id'], d['title'], d['completed']) for d in todos]
# pprint(todo_objects[0].as_json())



