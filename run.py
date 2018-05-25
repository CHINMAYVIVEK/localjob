from flask import Flask, render_template

app = Flask(__name__)


if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = 5000, debug = True)
   app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'