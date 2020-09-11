from app import app
from flask import render_template, request


@app.route('/', methods=['POST', 'GET'])
def index():
    link = ''
    new_link = ''

    if request.method == 'POST':
        data = request.form
        link = data['link']
        new_link = link

    return render_template('index.html', link=link, new_link=new_link)
