from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/')
def echo():
    kargs = {}
    kargs['thing'] = request.args.get('thing')
    kargs['place'] = request.args.get('place')
    return render_template('flask3.html',**kargs)

app.run(port=9999, debug=True)

