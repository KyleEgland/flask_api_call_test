from flask import render_template
from flask import request
from flask import jsonify
from app.main import bp
import requests


# @bp.before_app_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.last_seen = datetime.utcnow()
#         db.session.commit()
#     g.locale = str(get_locale())


@bp.route('/')
@bp.route('/index')
def index():
    # Render index
    return render_template('apitest.html')


@bp.route('/gettoken', methods=['POST'])
def gettoken():
    # The caller should be our javascript apt which will pass in a dictionary
    request_info = request.data()

    target = request_info['target']

    headers = request_info['headers']

    auth_req = requests.post(target, headers=headers, verify=False)

    status = auth_req.status_code

    auth_req.encoding = 'utf-8'

    json_resp = {
        'status': status,
        'response': auth_req.text
    }

    return jsonify(json_resp)


@bp.route('/getapirequest', methods=['POST'])
def getapirequest():
    pass
