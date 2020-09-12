from app import app
from app import config
from flask import g
import sqlite3


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(config.DATABASE)
    return db

def add_uri(uri, link):
    db = get_db()

    c = db.cursor()
    c.execute('INSERT INTO urls(uri, link) values(?, ?)', (uri, link))
    
    db.commit()
    db.close()

def get_link(uri):
    db = get_db()

    c = db.cursor()
    c.execute('SELECT link FROM urls WHERE uri = ?', (uri,))
    link = c.fetchone()
    
    db.commit()
    db.close()

    return link[0] if link else None

@app.teardown_appcontext
def close_connection(e):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
