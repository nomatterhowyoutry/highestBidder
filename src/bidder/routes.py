from app import app
from .service import procces_request


@app.route('/bidder', methods=['GET'])
def bidder():
    return procces_request()
