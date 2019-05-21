from flask import render_template
from flask import request
from flask import jsonify
from app.main import bp
import requests
import json


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
    if request.get_json():
        content = request.get_json()

        return jsonify({'test_response': 'data exists',
                        'test_data': content['target']})

    # target = request_info['target']
    #
    # headers = request_info['headers']
    #
    # auth_req = requests.post(target, headers=headers, verify=False)
    #
    # status = auth_req.status_code
    #
    # auth_req.encoding = 'utf-8'

    # json_resp = {
    #     'test_response': request_info,
    # }

    else:
        return jsonify({'test_response': 'an error happend'})


@bp.route('/getapirequest', methods=['POST'])
def getapirequest():
    pass
