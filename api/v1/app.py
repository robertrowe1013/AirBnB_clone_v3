#!/usr/bin/python3
"""flask"""
from flask import Flask, render_template, jsonify
from models import storage
from api.v1.views import app_views
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(self):
    """teardown"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """404ed"""
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, threaded=True)
