from flask import Flask, render_template

from livereload import Server

app = Flask(__name__)


@app.route('/')
def homepage():  # put application's code here
    return render_template('homepage.html')

@app.route('/kedou')
def kedou():
    return render_template('kedou.html')

@app.route('/BEfunnyman')
def BEfunnyman():
    return render_template('BEfunnyman.html')



if __name__ == '__main__':
    app.debug = True
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve()
    app.run()
