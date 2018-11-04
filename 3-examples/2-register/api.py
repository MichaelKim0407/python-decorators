from app import app

__author__ = 'Michael'


@app.route('/api/')
def api_root():
    return "This api contains ..."
