from app import app
from flask import render_template, request, redirect, url_for
from app.functions import generate_uri
from app.database import add_uri, get_link


@app.route('/', methods=['POST', 'GET'])
def index():
    link = ''
    new_link = ''

    if request.method == 'POST':
        data = request.form
        link = data['link'].replace('http://', '').replace('https://', '')
        uri = generate_uri()
        new_link = uri
        add_uri(uri, link)
        new_link = 'http://94.103.88.55:5000/uri/' + uri

    return render_template('index.html', link=link, new_link=new_link)

@app.route('/uri/<uri>')
def uri_(uri):
    link = get_link(uri)
    print(link)
    if link is not None:
        return redirect('http://' + link)
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))
