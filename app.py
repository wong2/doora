#-*-coding:utf-8-*-

from flask import Flask, render_template, request, jsonify
from config import BUCKET_NAME, CALLBACK_URL, Q_DOMAIN, NEED_EXPIRE
from q import qiniu

app = Flask(__name__)


@app.route('/')
def index():
    policy = qiniu.rs.PutPolicy(BUCKET_NAME)
    policy.callbackBody = 'key=$(x:key)'
    policy.callbackUrl = CALLBACK_URL
    up_token = policy.token()

    return render_template('index.html', up_token=up_token)


@app.route('/callback', methods=['POST'])
def upload_callback():
    key = request.form['key']
    download_url = qiniu.rs.make_base_url(Q_DOMAIN, key)

    if NEED_EXPIRE:
        from cleaner import add_to_expire_queue
        add_to_expire_queue(key)

    return jsonify(download_url=download_url)


if __name__ == '__main__':
    app.run(debug=True)

