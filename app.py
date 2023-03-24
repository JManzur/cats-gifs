import urllib3
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)
http = urllib3.PoolManager()
app_version = "v1.0"

# list of cat images
images = [
    "https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif",
    "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif",
    "https://media.giphy.com/media/3nbxypT20Ulmo/giphy.gif",
    "https://media.giphy.com/media/CjmvTCZf2U3p09Cn0h/giphy.gif",
    "https://media.giphy.com/media/l6Td5sKDNmDGU/giphy.gif",
    "https://media.giphy.com/media/CqVNwrLt9KEDK/giphy.gif",
    "https://media.giphy.com/media/fjxMEdpMT9qDyBVLL4/giphy.gif",
    "https://media.giphy.com/media/8JIRQqil8mvEA/giphy.gif",
    "https://media.giphy.com/media/26n6xF5M2Ht4eKdO0/giphy.gif",
    "https://media.giphy.com/media/xH7Yh3DSNvn4k/giphy.gif",
    "https://media.giphy.com/media/GeimqsH0TLDt4tScGw/giphy.gif",
    "https://media.giphy.com/media/Nm8ZPAGOwZUQM/giphy.gif"
]

@app.route('/status')
def status():
    try:
        # Check if media.giphy.com is available
        response = http.request('GET', 'https://giphy.com/')

        if response.status == 200:
            return jsonify({
                'status': 'OK',
                'http_status': response.status,
                }), 200
        else:
            return jsonify({
                'status': 'ERROR giphy.com is not available',
                'http_status': response.status,
                }), 503
    except Exception as e:
        return jsonify({
            'status': 'ERROR giphy.com is not available',
            'error_message': '{0}'.format(str(e))
        }), 503

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url, version=app_version)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)