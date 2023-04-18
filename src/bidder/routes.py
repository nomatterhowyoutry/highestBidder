from app import app
from .service import procces_request
from flask import request


@app.route('/bidder', methods=['GET'])
def bidder():
    ip = request.args.get('ip')
    user_agent = request.args.get('ua')
    return procces_request()
