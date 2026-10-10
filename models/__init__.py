import sqlite3

from flask import current_app, g


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(_error=None):
    database = g.pop("db", None)
    if database is not None:
        database.close()


def init_db():
    with current_app.open_resource("database/schema.sql") as schema:
        get_db().executescript(schema.read().decode("utf-8"))


def init_app(app):
    app.teardown_appcontext(close_db)
    with app.app_context():
        init_db()

