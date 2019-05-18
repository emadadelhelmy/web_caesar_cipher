from flask import Flask, render_template, request
from string import ascii_lowercase as lc

application = Flask(__name__)


@application.route("/", methods=['GET'])
def index():
    content = render_template('form.html')
    return content


@application.route("/", methods=['POST'])
def crypt():
    result = ''
    text = request.form.get('text').lower()
    shift = int(request.form.get('shift'))
    if request.form.get('decrypt'):
        for c in text:
            if c in lc:
                result += lc[(lc.find(c) - shift) % len(lc)]
            else:
                result += c
    content = render_template('/form.html', text=text, shift=shift,
                              result=result)
    return content
if __name__ =="__main__":
    application.run()