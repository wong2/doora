#-*-coding:utf-8-*-

from flask import Flask, render_template, request, jsonify
from qiniu import Auth
from config import BUCKET_NAME, CALLBACK_URL, Q_DOMAIN, EXPIRE_TIME, ACCESS_KEY, SECRET_KEY

q = Auth(ACCESS_KEY, SECRET_KEY)
app = Flask(__name__)


@app.route('/')
def index():
    policy = {
        'callbackUrl': CALLBACK_URL,
        'callbackBody': 'key=$(key)',
        'deleteAfterDays': EXPIRE_TIME,
    }
    token = q.upload_token(BUCKET_NAME, policy)
    return render_template('index.html', token=token)


@app.route('/callback', methods=['POST'])
def upload_callback():
    key = request.form['key']
    base_url = 'http://%s/%s' % (Q_DOMAIN, key)
    download_url = q.private_download_url(base_url)
    return jsonify(download_url=download_url)


if __name__ == '__main__':
    app.run(debug=True)
