from app import app
import api  # try removing this line and then visit /api

__author__ = 'Michael'


@app.route('/')
def index():
    return '<a href="/api">api</a>'


if __name__ == '__main__':
    app.run()
