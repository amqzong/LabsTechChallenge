from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/amz2136', methods=['GET', 'POST'])
def index():
    return render_template('amz2136bio.html')

if __name__ == '__main__':
    app.run()
