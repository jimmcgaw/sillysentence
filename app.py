from flask import Flask, render_template, send_from_directory, jsonify
app = Flask(__name__, static_url_path='')

from generator import random_subject, random_predicate

@app.route('/')
def index():
    return render_template('index.html')


# hack for development, routes should be handled by web server in production
@app.route('/static/<path:filename>')
def send_static(filename):
    return send_from_directory('static', filename)

@app.route('/sentence')
def sentence():
    silly = {
        'subject': random_subject(),
        'predicate': random_predicate()
    }
    return jsonify(**silly)


if __name__ == "__main__":
    app.run()
