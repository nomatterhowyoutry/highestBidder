from app import app
from .service import process_request


@app.route('/auction')
def auction():
    return process_request()
