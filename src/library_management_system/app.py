# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from config import Config

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

members = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(member["id"] for member in members) + 1

@app.get("/members")
def get_members():
    return jsonify(members)

@app.post("/members")
def add_member():
    if request.is_json:
        member = request.get_json()
        member["id"] = _find_next_id()
        members.append(member)
        return member, 201
    return {"error": "Request must be JSON"}, 415

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Registering blueprints 
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8000, debug=True)    
    app.run(host="0.0.0.0", port=8000, debug=True)
    