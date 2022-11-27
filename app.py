from flask import Flask, render_template
from videos import videos, kedou_wutai, kedou_wutai_n, kedou_mcm, kedou_mcm_n
from livereload import Server

app = Flask(__name__)


@app.route('/')
def homepage():  # put application's code here
    return render_template('homepage.html')


@app.route('/kedou')
def kedou():
    return render_template('kedou.html', kedou_wutai=kedou_wutai, kedou_wutai_n=kedou_wutai_n, kedou_mcm=kedou_mcm,
                           kedou_mcm_n=kedou_mcm_n)


@app.route('/BEfunnyman')
def BEfunnyman():
    return render_template('BEfunnyman.html')


@app.route('/bigcandy')
def bigcandy():
    return render_template('bigcandy.html')


@app.route('/jianlaji')
def jianlaji():
    return render_template('jianlaji.html')


@app.route('/talkroom')
def talkroom():
    return render_template('talkroom.html')


if __name__ == '__main__':
    app.debug = True
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve()
    app.run()
