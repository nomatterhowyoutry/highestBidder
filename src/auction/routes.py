from app import app
from .service import process_request
from flask import request


@app.route('/auction', methods=['GET'])
def auction():
    ip = request.args.get('ip')
    user_agent = request.args.get('ua')
    partner_id = request.args.get('partner_id')
    return process_request()
